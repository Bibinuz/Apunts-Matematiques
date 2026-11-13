#!/usr/bin/env python3
"""
generar_llibre.py — Compila els apunts en un llibre complet o per cursos (HTML / PDF).
Ús:
  python3 scripts/generar_llibre.py                  # Tot el grau (Llibre_Matematiques.html)
  python3 scripts/generar_llibre.py --curs 1         # Només 1r Curs (Llibre_1r_Curs.html)
  python3 scripts/generar_llibre.py --curs 2         # Només 2n Curs (Llibre_2n_Curs.html)
  python3 scripts/generar_llibre.py -a "Algebra 1"   # Només una assignatura

Característiques clau:
- Suport per a l'estructura modular d'arbres per Curs (Apunts/<Curs>/<Assignatura>/).
- Descoberta 100% dinàmica d'assignatures i capítols (sense diccionaris rígidament 'hardcoded').
- Opcions de compilació per Curs, Assignatura individual o Compendi complet.
- Resolució de Wikilinks d'Obsidian a ancoratges interns clicables (<a href="#cap-...">).
- Filtratge automàtic de diagrames Mermaid i enllaços de navegació Obsidian.
- Protecció avançada de LaTeX ($ i $$) i renderització amb KaTeX.
- Estilisme pur de llibre acadèmic amb regles CSS per a impressió en PDF.
"""

import re
import argparse
import unicodedata
from pathlib import Path
from datetime import datetime
import markdown

BASE_DIR = Path(__file__).resolve().parent.parent
APUNTS_DIR = BASE_DIR / "Apunts"
INDEX_MASTER = BASE_DIR / "Índex.md"
DEFAULT_OUTPUT_FILE = BASE_DIR / "Llibre_Matematiques.html"
CSS_FILE = Path(__file__).resolve().parent / "estils_llibre.css"

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

    # 3. Elimina enllaços de navegació / relacionats de final de nota (admet qualsevol posició dels dos punts i asteriscs)
    pattern_enllacos = r"(?is)(?:\n\s*---\s*)*\n*\s*(?:#{1,4}\s*)?\*+Enllaços(?:\s+de\s+navegaci[oó]|\s+relacionats)[^\n]*\*+:?.*$"
    text = re.sub(pattern_enllacos, "", text).strip()

    # 4. Elimina separadors horitzontals orfes (---) al final del document
    text = re.sub(r"(?:\n\s*---\s*)+$", "", text).strip()

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


def descobrir_estructura_apunts(filtre_curs=None, filtre_assignatura=None):
    """
    Descobreix automàticament tots els cursos, assignatures i notes d'Apunts/.
    Suporta la jerarquia modular:
      Apunts/<Curs>/<Assignatura>/
    on cada assignatura conté les seves notes i el seu Índex - <Assignatura>.md.
    """
    master_order = []
    if INDEX_MASTER.exists():
        try:
            content = INDEX_MASTER.read_text(encoding="utf-8")
            matches = re.findall(r"\[\[(?:Índex\s*-\s*)?([^\|\]]+)(?:\|([^\]]+))?\]\]", content)
            for m in matches:
                target = m[0].strip()
                master_order.append(normalitzar_text(target))
        except Exception:
            pass

    # Detectar subdirectoris de cursos dins d'Apunts/
    course_dirs = [d for d in APUNTS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]
    course_dirs.sort(key=natural_sort_key)

    subjects_data = []

    for cdir in course_dirs:
        c_norm = normalitzar_text(cdir.name)

        # Aplicar filtre de curs si s'ha especificat
        if filtre_curs:
            f_norm = normalitzar_text(str(filtre_curs))
            # Comprova si coincideix amb el número o etiqueta ("1", "1r", etc.)
            if f_norm not in c_norm and (f_norm + "r") not in c_norm and (f_norm + "n") not in c_norm:
                continue

        # Llegir metadades de l'índex del curs si existeix
        curs_title = cdir.name
        curs_idx = cdir / f"Índex - {cdir.name}.md"
        if not curs_idx.exists():
            for f in cdir.glob("Índex - *.md"):
                curs_idx = f
                break
        if curs_idx.exists():
            try:
                m_t = re.search(r"^#\s+(?:Índex\s*[—–-]\s*)?(.+)$", curs_idx.read_text(encoding="utf-8"), re.MULTILINE)
                if m_t:
                    curs_title = m_t.group(1).strip()
            except Exception:
                pass

        # Buscar assignatures dins del curs
        subdirs = [d for d in cdir.iterdir() if d.is_dir() and not d.name.startswith(".")]

        # Si no hi ha subdirectoris de curs, suportar mode pla de compatibilitat
        if not subdirs:
            notes = [f for f in cdir.glob("*.md") if not f.name.startswith(".") and not f.name.startswith("Índex")]
            if notes:
                subdirs = [cdir]
                curs_title = "General"

        def get_order_key(d: Path):
            d_norm = normalitzar_text(d.name)
            if d_norm in master_order:
                return (0, master_order.index(d_norm))
            return (1, d.name)

        subdirs.sort(key=get_order_key)

        for d in subdirs:
            d_norm = normalitzar_text(d.name)

            # Aplicar filtre d'assignatura si s'ha especificat
            if filtre_assignatura:
                fa_norm = normalitzar_text(str(filtre_assignatura))
                if fa_norm not in d_norm:
                    continue

            # Buscar l'índex de l'assignatura DINS de la carpeta de l'assignatura
            matched_idx = None
            for idx_file in d.glob("Índex - *.md"):
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

            notes = [f for f in d.glob("*.md") if not f.name.startswith(".") and not f.name.startswith("Índex")]
            notes.sort(key=natural_sort_key)

            if notes:
                subjects_data.append({
                    "curs_code": cdir.name,
                    "curs_title": curs_title,
                    "dir_name": d.name,
                    "title": subject_title,
                    "desc": subject_desc,
                    "notes": notes
                })

    return subjects_data


def carregar_css() -> str:
    """Carrega el contingut del fitxer CSS d'estils. Si no existeix, retorna un missatge d'avís."""
    if CSS_FILE.exists():
        return CSS_FILE.read_text(encoding="utf-8")
    print(f"Avís: No s'ha trobat el fitxer d'estils CSS a {CSS_FILE}")
    return "/* Fitxer estils_llibre.css no trobat */"


def generar_html(parts: list, titol_llibre: str = "Compendi General de Matemàtiques", subtitol: str = "Apunts Teòrics, Teoremes i Demostracions") -> str:
    """Genera el document HTML complet amb portada, índex estilitzat i estil de llibre impecable."""
    now = datetime.now()
    data_str = f"{MESOS[now.month - 1]} de {now.year}"
    css_contingut = carregar_css()

    # 1. Taula de continguts global (TOC)
    toc = ['<div class="toc-container" id="taula-de-continguts">']
    toc.append('  <div class="toc-title">Taula de Continguts</div>')

    # Detectar si hi ha múltiples cursos
    distints_cursos = len(set(p.get("curs_title") for p in parts)) > 1
    current_curs = None

    for idx, part in enumerate(parts):
        curs = part.get("curs_title")
        if distints_cursos and curs and curs != current_curs:
            current_curs = curs
            toc.append(f'  <div class="toc-course-heading">{curs}</div>')

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

  <!-- Tipografia i estil de llibre (carregat des de scripts/estils_llibre.css) -->
  <style>
{css_contingut}
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
        <h1 class="cover-title">{titol_llibre}</h1>
        <div class="cover-divider"></div>
        <div class="cover-subtitle">{subtitol}</div>
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
    parser = argparse.ArgumentParser(
        description="Compila els apunts de Matemàtiques UAB en un llibre HTML/PDF."
    )
    parser.add_argument(
        "-c", "--curs",
        help="Filtra per curs (ex: 1, 2, '1r', '2n')."
    )
    parser.add_argument(
        "-a", "--assignatura",
        help="Filtra per nom d'assignatura (ex: 'Algebra 1', 'Funcions', 'Mecanica', 'Analisi')."
    )
    parser.add_argument(
        "-o", "--output",
        help="Ruta o nom del fitxer HTML de sortida."
    )
    parser.add_argument(
        "--tots",
        action="store_true",
        help="Compila totes les assignatures de tots els cursos (comportament per defecte)."
    )

    args = parser.parse_args()

    if not APUNTS_DIR.exists():
        print(f"Error: No s'ha trobat el directori d'apunts a: {APUNTS_DIR}")
        return

    # 1. Descoberta dinàmica d'assignatures i temes segons filtres
    subjects_data = descobrir_estructura_apunts(filtre_curs=args.curs, filtre_assignatura=args.assignatura)
    if not subjects_data:
        msg = "Error: No s'han trobat assignatures amb fitxers .md per als filtres indicats."
        if args.curs:
            msg += f" [Curs: '{args.curs}']"
        if args.assignatura:
            msg += f" [Assignatura: '{args.assignatura}']"
        print(msg)
        return

    # 2. Resolució de títols i fitxer de sortida
    if args.output:
        out_path = Path(args.output).resolve()
    elif args.assignatura and len(subjects_data) == 1:
        s_slug = slugify(subjects_data[0]["dir_name"])
        out_path = BASE_DIR / f"Llibre_{s_slug}.html"
    elif args.curs:
        c_slug = slugify(subjects_data[0]["curs_code"])
        out_path = BASE_DIR / f"Llibre_{c_slug}.html"
    else:
        out_path = DEFAULT_OUTPUT_FILE

    if args.assignatura and len(subjects_data) == 1:
        titol = f"{subjects_data[0]['title']}"
        subtitol = f"Apunts Teòrics i Demostracions · {subjects_data[0]['curs_title']}"
    elif args.curs:
        titol = f"Compendi de {subjects_data[0]['curs_title']}"
        mat_names = " · ".join([s["title"] for s in subjects_data])
        subtitol = mat_names if len(mat_names) < 120 else "Apunts Teòrics, Teoremes i Demostracions"
    else:
        titol = "Compendi General de Matemàtiques"
        subtitol = "Apunts Teòrics, Teoremes i Demostracions"

    print(f"Compilant llibre: '{titol}'...")

    # 3. Construcció del registre global de wikilinks (Stem -> cap_id)
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

    # 4. Processament de totes les parts i temes
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
            "curs_code": s.get("curs_code", ""),
            "curs_title": s.get("curs_title", ""),
            "title": s["title"],
            "dir_name": s["dir_name"],
            "desc": s["desc"],
            "chapters": chapters
        })

    # 5. Generació de l'HTML complet
    html = generar_html(parts, titol_llibre=titol, subtitol=subtitol)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Llibre generat correctament ({total_temes} temes de {len(parts)} assignatures inclosos) a:")
    print(f"   {out_path.resolve()}")
    print("\nPer obtenir el PDF:")
    print("   Obre el fitxer al navegador i prem el botó 'Desar en PDF' (o Ctrl + P).")


if __name__ == "__main__":
    main()
