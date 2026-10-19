# Guia d'Organització dels Apunts de Matemàtiques

Document normatiu d'estructura, estil i protocol d'incorporació de nous apunts.

---

## 1. Principis Fonamentals

1. **Unitat Conceptual (No Fragmentació):** Cada nota de Markdown cobreix un **tema o unitat conceptual completa** (no es creen fitxers per pàgina o foto).
2. **Fidelitat Absoluta a les Fotos (100%):** Es transcriu **únicament** el que s'ha impartit a classe. Prohibit afegir temari extern o anticipat de llibres de text.
3. **Correcció d'Errors de Pissarra:** Si es detecta una errada lògica, de signe, d'índexs o aritmètica a la pissarra, es corregeix al text per garantir el rigor matemàtic i s'indica obligatòriament amb el callout:
   ```markdown
   > [!NOTE] Nota de correcció lògica
   > Als apunts originals de pissarra constava ..., però s'ha corregit per ... atès que ...
   ```
4. **Interconnexió:** Ús sistemàtic d'enllaços interns d'Obsidian (`[[Nom de la Nota]]`) i actualització coordinada dels índexs.

---

## 2. Esquema de Directoris (Genèric)

```text
Matematiques/
├── GUIA_APUNTS.md
├── Apunts Fotos/
│   ├── registre_fotos.csv          # Registre de seguiment de fotos processades
│   └── <NomAssignatura>/           # Fotos originals de classe (no esborrar mai)
└── Apunts/
    ├── Índex.md                    # Hub d'accés principal (totes les assignatures)
    ├── Índex - <Assignatura>.md    # Índex temàtic per assignatura
    └── <NomAssignatura>/           # Subcarpetes per matèria
        └── <NN>. <Títol del Tema>.md
```

---

## 3. Convencions de Format

* **$\LaTeX$:** Fórmules en línia amb `$x \in \mathbb{R}$` i en bloc amb `$$...$$`. Finalitzar demostracions amb `\blacksquare`. Conjunts estàndard: `\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{K}`.
* **Callouts d'Obsidian:**
  * `> [!IMPORTANT] Teorema / Definició`: Resultats clau, axiomes i definicions.
  * `> [!NOTE] Proposició / Lema / Nota de correcció lògica`: Resultats derivats i esmenes de classe.
  * `> [!WARNING] Atenció`: Casos que indueixen a error o convenis especials.
  * `> [!TIP] Intuïció`: Interpretacions geomètriques o mètodes de resolució pràctics.
* **Navegació:** Al final de cada nota s'inclouen enllaços a l'`[[Índex]]`, tema anterior i tema posterior.

---

## 4. Protocol d'Incorporació de Noves Fotos

1. **Desar les imatges:** Afegir les fotos a `Apunts Fotos/<NomAssignatura>/` (orientades i llegibles).
2. **Triar destí (evitar fragmentació):**
   * *Continuació de tema:* Ampliar la nota existent.
   * *Nou tema:* Crear `<NN+1>. <Nom del Nou Tema>.md`.
3. **Transcripció:** Transcriure amb rigor pas a pas en $\LaTeX$, fidelitat 100% a les fotografies i callouts de correcció si escau.
4. **Actualitzar índexs i registre:**
   * Actualitzar `Índex - <Assignatura>.md` i `Índex.md`.
   * Registrar les fotos com a `Processat` a `Apunts Fotos/registre_fotos.csv`.
