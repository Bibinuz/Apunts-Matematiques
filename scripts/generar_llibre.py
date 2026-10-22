#!/usr/bin/env python3
"""
generar_llibre.py — Compila tots els apunts en un únic llibre complet (HTML / PDF).
Ús: python3 scripts/generar_llibre.py

Característiques clau:
- Descoberta 100% dinàmica d'assignatures i capítols (sense diccionaris rígidament 'hardcoded').
- Suport per a qualsevol quantitat d'assignatures amb numeració romana algorítmica.
- Resolució de Wikilinks d'Obsidian a ancoratges interns clicables (<a href="#cap-...">).
- Filtratge automàtic de notes d'esmena i diagrames Mermaid (treball en brut d'Obsidian).
- Protecció avançada de LaTeX ($ i $$) i normalització de llistes en blocs de teories/callouts.
- Estilisme pur natiu (CSS autònom sense dependències de JS invasiu com Paged.js).
- Regles de print CSS (@media print) per a impressió neta en PDF (salts de pàgina, protecció de fórmules).
"""

import re
import unicodedata
from pathlib import Path
from datetime import datetime
import markdown

BASE_DIR = Path(__file__).resolve().parent.parent
APUNTS_DIR = BASE_DIR / "Apunts"
OUTPUT_FILE = BASE_DIR / "Llibre_Matematiques.html"

MESOS = [
    "Gener", "Febrer", "Març", "Abril", "Maig", "Juny",
    "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"
]

CALLOUT_DEFAULTS = {
    "IMPORTANT": ("callout-important", "TEOREMA / DEFINICIÓ"),
    "NOTE": ("callout-note", "PROPOSICIÓ / LEMA"),
    "WARNING": ("callout-warning", "ATENCIÓ"),
    "TIP": ("callout-tip", "INTUÏCIÓ"),
    "CAUTION": ("callout-warning", "ALERTA"),
    "EXAMPLE": ("callout-tip", "EXEMPLE")
}


def normalitzar_text(s: str) -> str:
    """Elimina accents, espais i caràcters especials per a comparacions robustes."""
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-zA-Z0-9]', '', s.lower())


def slugify(text: str) -> str:
    """Genera un slug URL/HTML net i segur a partir d'un text."""
    s = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^\w\s-]', '', s.lower()).strip()
    return re.sub(r'[-\s]+', '-', s)


def to_roman(n: int) -> str:
    """Converteix qualsevol enter positiu a xifres romanes."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = []
    for v, s in zip(val, syb):
        while n >= v:
            res.append(s)
            n -= v
    return "".join(res) if res else "I"


def natural_sort_key(path: Path):
    """Clau d'ordenació numèrica natural per a fitxers tipus '01. Nom', '02. Nom'."""
    m = re.match(r"^(\d+)", path.stem)
    if m:
        return (int(m.group(1)), path.stem)
    return (999, path.stem)


def netejar_contingut(text: str) -> str:
    """
    Elimina diagrames Mermaid, apartats d'esquema resum i enllaços de navegació de final de nota.
    Els wikilinks es preserven perquè seran resolts a ancoratges interns.
    """
    # 1. Elimina blocs Mermaid
    text = re.sub(r"```mermaid[\s\S]*?```", "", text)

    # 2. Elimina apartats d'esquema/resum que només servien per al diagrama
    text = re.sub(r"(?m)^##\s*\d*\.?\s*Esquema\s+(Resum|Global).*$", "", text)

    # 3. Elimina enllaços de navegació de final de nota
    text = re.sub(r"(?s)(---\s*)?\*+(Enllaços de navegació|Enllaços relacionats)\*+:?.*$", "", text).strip()

    return text


def protegir_i_convertir_markdown(text: str, wikilink_registry: dict = None) -> str:
    """
    Processa el Markdown protegint fórmules LaTeX ($ i $$) i blocs de codi.
    Resol els wikilinks d'Obsidian a enllaços interns HTML i normalitza les llistes.
    """
    if wikilink_registry is None:
        wikilink_registry = {}

    # 1. Protegir els signes de dòlar ($) que es trobin dins de blocs de codi
    def protect_code(m):
        return m.group(0).replace("$", "\uF000")

    def restore_code(m):
        return m.group(0).replace("\uF000", "$")

    text = re.sub(r"```[\s\S]*?```", protect_code, text)
    text = re.sub(r"`[^`\n]+?`", protect_code, text)

    # 2. Extreure i protegir fórmules LaTeX
    math_tokens = []

    def save_math(m):
        math_tokens.append(m.group(0))
        return f"@@M_TOKEN_{len(math_tokens)-1}@@"

    # Display math ($$...$$)
    text = re.sub(r"\$\$[\s\S]*?\$\$", save_math, text)
    # Inline math ($...$) amb suport per a caràcters escapats i salts de línia
    text = re.sub(r"(?<!\$)\$(?!\$)(?:\\.|[^\$\\])+?\$", save_math, text)

    # Restaurar codi abans de passar pel motor Markdown
    text = re.sub(r"```[\s\S]*?```", restore_code, text)
    text = re.sub(r"`[^`\n]+?`", restore_code, text)

    # 3. Resolució de Wikilinks d'Obsidian
    def repl_wikilink(m):
        raw_target = m.group(1).strip()
        label = m.group(2).strip() if m.group(2) else raw_target

        base_target = raw_target.split("#")[0].strip()
        target_id = wikilink_registry.get(base_target)
        if not target_id:
            target_norm = normalitzar_text(base_target)
            for reg_name, reg_id in wikilink_registry.items():
                if normalitzar_text(reg_name) == target_norm:
                    target_id = reg_id
                    break

        if target_id:
            return f'<a href="#{target_id}" class="internal-link">{label}</a>'
        return label

    text = re.sub(r"\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]", repl_wikilink, text)

    # 4. Normalització de llistes (assegurar salt de línia previ per a Python-Markdown)
    lines = text.split("\n")
    norm_lines = []
    for idx, line in enumerate(lines):
        if idx > 0 and re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line):
            prev = lines[idx - 1]
            if prev.strip() and not re.match(r"^\s*(?:[-*+]|\d+\.)\s+", prev):
                norm_lines.append("")
        norm_lines.append(line)
    text = "\n".join(norm_lines)

    # 5. Conversió de Markdown a HTML
    html = markdown.markdown(text, extensions=["fenced_code", "tables", "def_list", "attr_list"])

    # 6. Reintegrar les fórmules LaTeX escapant < i > perquè KaTeX les rebi com a TextNodes purs
    for idx, token in enumerate(math_tokens):
        escaped_math = token.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html = html.replace(f"@@M_TOKEN_{idx}@@", escaped_math)

    return html


def get_callout_badge_and_class(ctype: str, ctitle: str):
    """Determina la insígnia semàntica i la classe d'estil exacta per a un callout."""
    lower_t = ctitle.lower()

    if lower_t.startswith("teorema"):
        return "callout-important", "TEOREMA"
    if lower_t.startswith("definició") or lower_t.startswith("definicio"):
        return "callout-important", "DEFINICIÓ"
    if lower_t.startswith("proposició") or lower_t.startswith("proposicio"):
        return "callout-note", "PROPOSICIÓ"
    if lower_t.startswith("lema"):
        return "callout-note", "LEMA"
    if lower_t.startswith("corol·lari") or lower_t.startswith("corollari"):
        return "callout-note", "COROL·LARI"
    if lower_t.startswith("observació") or lower_t.startswith("observacio"):
        return "callout-note", "OBSERVACIÓ"
    if lower_t.startswith("exemple"):
        return "callout-tip", "EXEMPLE"
    if lower_t.startswith("atenció") or lower_t.startswith("atencio"):
        return "callout-warning", "ATENCIÓ"
    if lower_t.startswith("intuïció") or lower_t.startswith("intuicio"):
        return "callout-tip", "INTUÏCIÓ"

    return CALLOUT_DEFAULTS.get(ctype, ("callout-note", ctype))


def processar_callouts(text: str, wikilink_registry: dict):
    """
    Extreu els callouts d'Obsidian, filtra notes d'esmena i converteix el cos interior a HTML.
    Tolerant a múltiples línies en blanc consecutives dins del callout.
    """
    lines = text.split("\n")
    out = []
    callouts_html = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = re.match(r"^>\s*\[!([a-zA-Z_-]+)\]\s*(.*)$", line)
        if m:
            ctype = m.group(1).upper()
            ctitle = m.group(2).strip()

            # Filtrar notes d'esmena segons indicació
            is_esmena = "esmena" in ctitle.lower() or "esmena" in ctype.lower()

            body = []
            i += 1
            while i < len(lines):
                cur = lines[i]
                # Si comença un nou callout, finalitzar l'actual
                if re.match(r"^>\s*\[!([a-zA-Z_-]+)\]", cur):
                    break

                if cur.startswith(">"):
                    body.append(re.sub(r"^>\s?", "", cur))
                    i += 1
                elif cur.strip() == "":
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and lines[j].startswith(">") and not re.match(r"^>\s*\[!([a-zA-Z_-]+)\]", lines[j]):
                        while i < j:
                            body.append("")
                            i += 1
                    else:
                        break
                else:
                    break

            if is_esmena:
                continue

            cls_name, badge = get_callout_badge_and_class(ctype, ctitle)
            inner_md = "\n".join(body).strip()
            inner_html = protegir_i_convertir_markdown(inner_md, wikilink_registry)

            t_html = f"<span class='callout-title'>{ctitle}</span>" if ctitle else ""
            cid = len(callouts_html)
            callout_box = (
                f"<div class='callout {cls_name}'>\n"
                f"  <div class='callout-header'><span class='callout-badge'>{badge}</span> {t_html}</div>\n"
                f"  <div class='callout-body'>\n{inner_html}\n  </div>\n"
                f"</div>"
            )
            callouts_html.append(callout_box)
            out.append(f"\n\n%%CALLOUT_BLOCK_{cid}%%\n\n")
        else:
            out.append(line)
            i += 1

    return "\n".join(out), callouts_html


def processar_tema(filepath: Path, ch_id: str, wikilink_registry: dict):
    """Llegeix i processa un fitxer de tema individual."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    text = netejar_contingut(text)

    # 1. Títol del capítol (# ...)
    title_m = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    chapter_title = title_m.group(1).strip() if title_m else filepath.stem
    text = re.sub(r"^#\s+.+$", "", text, count=1, flags=re.MULTILINE).strip()

    # 2. Seccions (## ...) per a la Taula de Continguts
    sections = []
    sec_count = [0]

    def repl_sec(m):
        sec_count[0] += 1
        stitle = m.group(1).strip()
        sid = f"{ch_id}-sec-{sec_count[0]}"
        sections.append({"id": sid, "title": stitle})
        return f'<h3 id="{sid}" class="section-title">{stitle}</h3>'

    text = re.sub(r"^##\s+(.+)$", repl_sec, text, flags=re.MULTILINE)
    text = re.sub(r"^###\s+(.+)$", r'<h4 class="subsection-title">\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r"^####\s+(.+)$", r'<h5 class="subsubsection-title">\1</h5>', text, flags=re.MULTILINE)

    # 3. Processar callouts
    text, callouts_html = processar_callouts(text, wikilink_registry)

    # 4. Convertir el markdown general
    html = protegir_i_convertir_markdown(text, wikilink_registry)

    # 5. Reintegrar les caixes de callouts
    for cid, c_box in enumerate(callouts_html):
        html = html.replace(f"<p>%%CALLOUT_BLOCK_{cid}%%</p>", c_box)
        html = html.replace(f"%%CALLOUT_BLOCK_{cid}%%", c_box)

    return {
        "id": ch_id,
        "title": chapter_title,
        "sections": sections,
        "html": html
    }


def descobrir_estructura_apunts():
    """
    Descobreix automàticament totes les assignatures i notes d'Apunts/ sense llistes hardcoded.
    Preserva l'ordre establert a Índex.md si està present, i extreu metadades d'Índex - <Assignatura>.md.
    """
    index_master = APUNTS_DIR / "Índex.md"
    master_order = []
    if index_master.exists():
        try:
            content = index_master.read_text(encoding="utf-8")
            matches = re.findall(r"###\s*\d+\.\s*\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]", content)
            for target, _ in matches:
                clean_target = re.sub(r"^Índex\s*-\s*", "", target)
                master_order.append(normalitzar_text(clean_target))
        except Exception:
            pass

    index_files = list(APUNTS_DIR.glob("Índex - *.md"))
    subdirs = [d for d in APUNTS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]

    def get_order_key(d: Path):
        d_norm = normalitzar_text(d.name)
        if d_norm in master_order:
            return (0, master_order.index(d_norm))
        return (1, d.name)

    subdirs.sort(key=get_order_key)

    subjects_data = []

    for d in subdirs:
        d_norm = normalitzar_text(d.name)
        matched_idx = None
        for idx_file in index_files:
            m = re.match(r"Índex\s*-\s*(.+)\.md", idx_file.name)
            if m and normalitzar_text(m.group(1)) == d_norm:
                matched_idx = idx_file
                break

        subject_title = d.name
        subject_desc = ""

        if matched_idx and matched_idx.exists():
            try:
                idx_content = matched_idx.read_text(encoding="utf-8")
                m_title = re.search(r"^#\s+(?:Índex\s*[—–-]\s*)?(.+)$", idx_content, re.MULTILINE)
                if m_title:
                    subject_title = m_title.group(1).strip()

                lines = idx_content.strip().splitlines()
                desc_lines = []
                in_desc = False
                for l in lines:
                    sl = l.strip()
                    if sl.startswith("# ") and not in_desc:
                        in_desc = True
                        continue
                    if in_desc:
                        if re.match(r"^(?:---|___|\*\*\*|##)", sl):
                            break
                        desc_lines.append(l)
                subject_desc = "\n".join(desc_lines).strip()
            except Exception:
                pass

        notes = [f for f in d.glob("*.md") if not f.name.startswith(".")]
        notes.sort(key=natural_sort_key)

        if notes:
            subjects_data.append({
                "dir_name": d.name,
                "title": subject_title,
                "desc": subject_desc,
                "notes": notes
            })

    return subjects_data


def generar_html(parts: list) -> str:
    """Genera el document HTML complet amb portada, índex estilitzat i estil de llibre impecable."""
    now = datetime.now()
    data_str = f"{MESOS[now.month - 1]} de {now.year}"

    # 1. Taula de continguts global (TOC)
    toc = ['<div class="toc-container" id="taula-de-continguts">']
    toc.append('  <div class="toc-title">Taula de Continguts</div>')
    for idx, part in enumerate(parts):
        roman = to_roman(idx + 1)
        part_id = f"part-{idx + 1}"
        toc.append(f'  <div class="toc-part"><a href="#{part_id}">Part {roman} — {part["title"]}</a></div>')
        for ch in part["chapters"]:
            toc.append(f'  <div class="toc-chapter"><a href="#{ch["id"]}">{ch["title"]}</a></div>')
            if ch["sections"]:
                sec_links = [f'<a href="#{s["id"]}">{s["title"]}</a>' for s in ch["sections"]]
                toc.append(f'  <div class="toc-sections">{" · ".join(sec_links)}</div>')
    toc.append('</div>')

    # 2. Contingut de les parts i capítols
    body = []
    for idx, part in enumerate(parts):
        roman = to_roman(idx + 1)
        part_id = f"part-{idx + 1}"

        # Mini-índex de l'assignatura
        part_toc_cards = []
        for ch in part["chapters"]:
            sec_items = []
            for s in ch["sections"]:
                sec_items.append(f'<li><a href="#{s["id"]}"><strong>{s["title"]}</strong></a></li>')
            sec_html = f'<ul class="part-toc-sections">{"".join(sec_items)}</ul>' if sec_items else ""
            part_toc_cards.append(f'''
            <div class="part-toc-chapter">
              <div class="part-toc-chapter-title"><a href="#{ch["id"]}">{ch["title"]}</a></div>
              {sec_html}
            </div>
            ''')

        desc_html = protegir_i_convertir_markdown(part["desc"]) if part["desc"] else ""

        body.append(f'''
        <div class="part-page" id="{part_id}">
          <div class="part-header">
            <div class="part-number">Part {roman}</div>
            <h1 class="part-title">{part["title"]}</h1>
            <div class="part-rule"></div>
            {f'<div class="part-intro">{desc_html}</div>' if desc_html else ''}
          </div>

          <div class="part-toc">
            <div class="part-toc-title">Índex de la Matèria</div>
            <div class="part-toc-grid">
              {"".join(part_toc_cards)}
            </div>
          </div>
        </div>
        ''')

        for ch in part["chapters"]:
            body.append(f'''
            <section class="chapter" id="{ch["id"]}">
              <h2 class="chapter-title">{ch["title"]}</h2>
              <div class="chapter-body">
                {ch["html"]}
              </div>
            </section>
            ''')

    return f"""<!DOCTYPE html>
<html lang="ca">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grau de Matemàtiques — Compendi Teòric</title>

  <!-- Tipografia i estil de llibre -->
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@400;500;600;700&display=swap');

    :root {{
      --font-body: 'Crimson Pro', Georgia, serif;
      --font-heading: 'Inter', system-ui, -apple-system, sans-serif;
      --color-text: #1e293b;
      --color-primary: #0f172a;
      --color-border: #e2e8f0;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      padding: 0;
      background: #f8fafc;
      color: var(--color-text);
      font-family: var(--font-body);
      font-size: 11.5pt;
      line-height: 1.62;
      orphans: 2;
      widows: 2;
    }}

    .book-container {{
      max-width: 860px;
      margin: 30px auto;
      background: #ffffff;
      padding: 70px 80px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
      border-radius: 4px;
    }}

    h1, h2, h3, h4, h5 {{
      font-family: var(--font-heading);
      color: var(--color-primary);
      line-height: 1.25;
      margin-top: 1.6em;
      margin-bottom: 0.5em;
    }}

    h2.chapter-title {{
      font-size: 20pt;
      border-bottom: 1.5px solid var(--color-border);
      padding-bottom: 10px;
      margin-top: 40px;
    }}

    h3.section-title {{ font-size: 14pt; color: #1e3a8a; margin-top: 30px; }}
    h4.subsection-title {{ font-size: 12pt; color: #334155; margin-top: 20px; }}

    p {{ margin: 0 0 1em 0; text-align: justify; hyphens: auto; }}

    /* Enllaços interns */
    a.internal-link {{
      color: #2563eb;
      text-decoration: underline;
      text-decoration-thickness: 1px;
      text-underline-offset: 2px;
    }}
    a.internal-link:hover {{ color: #1d4ed8; text-decoration-thickness: 2px; }}

    /* Portada */
    .cover {{
      min-height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      padding: 60px 20px;
      border: 3px double #cbd5e1;
      margin-bottom: 50px;
    }}

    .cover-institution {{
      font-family: var(--font-heading);
      font-size: 11pt;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: #64748b;
    }}

    .cover-faculty {{
      font-family: var(--font-heading);
      font-size: 10pt;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #94a3b8;
      margin-top: 4px;
    }}

    .cover-degree {{
      font-family: var(--font-heading);
      font-size: 13pt;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--color-primary);
      margin-top: 10px;
    }}

    .cover-title {{
      font-size: 32pt;
      font-weight: 800;
      margin: 0 0 15px 0;
      color: var(--color-primary);
    }}

    .cover-divider {{
      width: 100px;
      height: 3px;
      background: #2563eb;
      margin: 20px auto;
    }}

    .cover-subtitle {{
      font-size: 14pt;
      color: #64748b;
      font-style: italic;
    }}

    .cover-footer {{
      font-family: var(--font-heading);
      font-size: 10pt;
      color: #64748b;
    }}

    /* TOC General */
    .toc-container {{
      margin: 40px 0 60px 0;
      padding: 30px 40px;
      background: #f8fafc;
      border: 1px solid var(--color-border);
      border-radius: 6px;
    }}

    .toc-title {{
      font-size: 17pt;
      font-family: var(--font-heading);
      text-align: center;
      margin-bottom: 25px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}

    .toc-part {{
      font-family: var(--font-heading);
      font-weight: 700;
      font-size: 12.5pt;
      margin-top: 20px;
      border-bottom: 1px dashed #cbd5e1;
      padding-bottom: 4px;
    }}

    .toc-part a {{
      color: var(--color-primary);
      text-decoration: none;
    }}

    .toc-part a:hover {{
      color: #2563eb;
      text-decoration: underline;
    }}

    .toc-chapter {{ margin-left: 15px; font-weight: 600; margin-top: 6px; }}
    .toc-chapter a {{ color: #2563eb; text-decoration: none; }}
    .toc-chapter a:hover {{ text-decoration: underline; }}
    .toc-sections {{ margin-left: 35px; font-size: 9.5pt; color: #64748b; line-height: 1.5; }}
    .toc-sections a {{ color: #475569; text-decoration: none; }}
    .toc-sections a:hover {{ color: #2563eb; text-decoration: underline; }}

    /* Pàgina de Matèria (Part) */
    .part-page {{
      margin: 40px 0 60px 0;
      padding: 30px 0 20px 0;
    }}

    .part-header {{
      margin-bottom: 25px;
    }}

    .part-number {{
      font-family: var(--font-heading);
      font-size: 11pt;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: #2563eb;
      margin-bottom: 6px;
    }}

    .part-title {{
      font-size: 26pt;
      font-weight: 800;
      color: var(--color-primary);
      margin: 0 0 10px 0;
      line-height: 1.2;
    }}

    .part-rule {{
      width: 60px;
      height: 3px;
      background: #2563eb;
      margin: 12px 0 18px 0;
    }}

    .part-intro {{
      font-size: 11pt;
      color: #475569;
      line-height: 1.6;
      text-align: justify;
    }}

    .part-intro p {{
      margin: 0;
    }}

    .part-toc {{
      background: #f8fafc;
      border: 1px solid var(--color-border);
      border-radius: 6px;
      padding: 24px 28px;
      margin-top: 25px;
    }}

    .part-toc-title {{
      font-family: var(--font-heading);
      font-size: 11pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #1e293b;
      margin-bottom: 16px;
      padding-bottom: 8px;
      border-bottom: 1px solid #cbd5e1;
    }}

    .part-toc-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px 30px;
    }}

    .part-toc-chapter {{
      break-inside: avoid;
    }}

    .part-toc-chapter-title {{
      font-family: var(--font-heading);
      font-size: 10pt;
      font-weight: 700;
      margin-bottom: 6px;
    }}

    .part-toc-chapter-title a {{
      color: #1e3a8a;
      text-decoration: none;
    }}

    .part-toc-chapter-title a:hover {{
      text-decoration: underline;
    }}

    .part-toc-sections {{
      margin: 0;
      padding-left: 18px;
      font-size: 9pt;
      line-height: 1.5;
    }}

    .part-toc-sections li {{
      margin-bottom: 3px;
    }}

    .part-toc-sections li a {{
      color: #334155;
      text-decoration: none;
      font-weight: 600;
    }}

    .part-toc-sections li a:hover {{
      color: #2563eb;
      text-decoration: underline;
    }}

    /* Callouts - Teoremes, Definicions, Proposicions */
    .callout {{
      margin: 1.4em 0;
      border-radius: 4px;
      border-left: 4.5px solid;
      background: #f8fafc;
      page-break-inside: auto;
      break-inside: auto;
    }}

    .callout-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 14px;
      font-family: var(--font-heading);
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
      page-break-after: avoid;
      break-after: avoid;
    }}

    .callout-badge {{
      font-size: 7.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 2.5px 7px;
      border-radius: 3px;
      color: white;
      display: inline-block;
    }}

    .callout-title {{
      font-family: var(--font-heading);
      font-size: 10pt;
      font-weight: 700;
      color: var(--color-primary);
    }}

    .callout-body {{
      padding: 12px 16px 6px 16px;
      page-break-inside: auto;
      break-inside: auto;
    }}
    .callout-body p:last-child {{ margin-bottom: 0; }}

    .callout-important {{ border-color: #2563eb; background: #f8faff; }}
    .callout-important .callout-header {{ background: #edf2fe; color: #1e40af; }}
    .callout-important .callout-badge {{ background: #2563eb; }}

    .callout-note {{ border-color: #0284c7; background: #f0f9ff; }}
    .callout-note .callout-header {{ background: #e0f2fe; color: #0369a1; }}
    .callout-note .callout-badge {{ background: #0284c7; }}

    .callout-warning {{ border-color: #d97706; background: #fffbeb; }}
    .callout-warning .callout-header {{ background: #fef3c7; color: #92400e; }}
    .callout-warning .callout-badge {{ background: #d97706; }}

    .callout-tip {{ border-color: #059669; background: #f0fdf4; }}
    .callout-tip .callout-header {{ background: #dcfce7; color: #065f46; }}
    .callout-tip .callout-badge {{ background: #059669; }}

    table {{ width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 10.5pt; page-break-inside: auto; break-inside: auto; }}
    tr {{ page-break-inside: avoid; break-inside: avoid; }}
    th, td {{ border: 1px solid var(--color-border); padding: 8px 12px; }}
    th {{ background: #f8fafc; font-family: var(--font-heading); }}

    /* Botó per imprimir (pantalla) */
    .screen-toolbar {{
      position: fixed;
      bottom: 25px;
      right: 25px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 1000;
    }}

    .toolbar-hint {{
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      color: #f8fafc;
      padding: 9px 15px;
      border-radius: 20px;
      font-family: var(--font-heading);
      font-size: 9pt;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      pointer-events: none;
    }}

    .btn-print {{
      background: #0f172a;
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 30px;
      font-family: var(--font-heading);
      font-size: 10.5pt;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
      transition: all 0.2s;
    }}

    .btn-print:hover {{ background: #2563eb; transform: translateY(-2px); }}

    /* Impressió en PDF */
    @media print {{
      body {{ background: white !important; font-size: 10.5pt; }}
      .book-container {{ max-width: 100% !important; padding: 0 !important; margin: 0 !important; box-shadow: none !important; }}
      .screen-toolbar {{ display: none !important; }}
      @page {{
        size: A4;
        margin: 2.2cm 1.8cm 2.2cm 1.8cm;
      }}
      .cover {{ height: 100vh; margin: 0; page-break-after: always; break-after: page; }}
      .toc-container {{ page-break-before: always; break-before: page; page-break-after: always; break-after: page; }}
      .part-page {{
        page-break-before: always;
        break-before: page;
        page-break-inside: avoid;
        break-inside: avoid;
        margin: 0;
        padding: 25px 0;
      }}
      .part-toc {{
        background: #ffffff !important;
        border: 1px solid #cbd5e1;
      }}
      .chapter {{ page-break-before: always; break-before: page; }}
      .katex-display {{
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }}
      .callout {{
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }}
      .callout-header {{
        page-break-after: avoid !important;
        break-after: avoid !important;
      }}
      .callout-body {{
        page-break-inside: auto !important;
        break-inside: auto !important;
      }}
      table {{ page-break-inside: auto; break-inside: auto; }}
      tr {{ page-break-inside: avoid; break-inside: avoid; }}
      h2, h3, h4 {{ page-break-after: avoid; break-after: avoid; }}
    }}
  </style>

  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}}
            ],
            throwOnError: false
          }});"></script>
</head>
<body>

  <div class="screen-toolbar">
    <div class="toolbar-hint">Recorda desmarcar <strong>"Capçaleres i peus de pàgina"</strong> al diàleg d'impressió</div>
    <button onclick="window.print()" class="btn-print">Desar en PDF</button>
  </div>

  <div class="book-container">
    <!-- Portada -->
    <div class="cover">
      <div class="cover-institution">
        <div>Universitat Autònoma de Barcelona</div>
        <div class="cover-faculty">Facultat de Ciències</div>
        <div class="cover-degree">Grau de Matemàtiques</div>
      </div>
      <div class="cover-main">
        <h1 class="cover-title">Compendi General de Matemàtiques</h1>
        <div class="cover-divider"></div>
        <div class="cover-subtitle">Apunts Teòrics, Teoremes i Demostracions</div>
      </div>
      <div class="cover-footer">
        <div>Facultat de Ciències · Universitat Autònoma de Barcelona</div>
        <div>{data_str}</div>
      </div>
    </div>

    <!-- Índex General -->
    {"".join(toc)}

    <!-- Parts i Capítols -->
    {"".join(body)}
  </div>

</body>
</html>
"""


def main():
    if not APUNTS_DIR.exists():
        print(f"Error: No s'ha trobat el directori d'apunts a: {APUNTS_DIR}")
        return

    print("Compilant tots els apunts en un únic llibre...")

    # 1. Descoberta dinàmica d'assignatures i temes
    subjects_data = descobrir_estructura_apunts()
    if not subjects_data:
        print("Error: No s'han trobat assignatures amb fitxers .md a Apunts/")
        return

    # 2. Construcció del registre global de wikilinks (Stem -> cap_id)
    wikilink_registry = {}
    total_notes_plan = 0

    for s_idx, s in enumerate(subjects_data):
        subj_slug = slugify(s["dir_name"])
        for n in s["notes"]:
            total_notes_plan += 1
            m_num = re.match(r"^(\d+)", n.stem)
            num_str = f"{int(m_num.group(1)):02d}" if m_num else f"{total_notes_plan:02d}"
            cid = f"cap-{subj_slug}-{num_str}"

            # Registre pel nom complet del fitxer sense extensió
            wikilink_registry[n.stem] = cid
            # Registre net sense el prefix numèric ("01. Sistemes Lineals..." -> "Sistemes Lineals...")
            clean_stem = re.sub(r"^\d+\.\s*", "", n.stem)
            if clean_stem != n.stem:
                wikilink_registry[clean_stem] = cid

    # 3. Processament de totes les parts i temes
    parts = []
    total_temes = 0

    for s in subjects_data:
        subj_slug = slugify(s["dir_name"])
        chapters = []

        for n in s["notes"]:
            cid = wikilink_registry[n.stem]
            chapters.append(processar_tema(n, cid, wikilink_registry))
            total_temes += 1

        parts.append({
            "title": s["title"],
            "dir_name": s["dir_name"],
            "desc": s["desc"],
            "chapters": chapters
        })

    # 4. Generació de l'HTML complet
    html = generar_html(parts)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Llibre generat correctament ({total_temes} temes de {len(parts)} assignatures inclosos) a:")
    print(f"   {OUTPUT_FILE.resolve()}")
    print("\nPer obtenir el PDF:")
    print("   Obre el fitxer al navegador i prem el botó 'Desar en PDF' (o Ctrl + P).")


if __name__ == "__main__":
    main()
