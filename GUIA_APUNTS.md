# Guia d'Organització dels Apunts de Matemàtiques

Bones pràctiques, convencions d'estil i protocol per redactar i actualitzar els apunts del grau de forma col·laborativa.

---

## 1. Principis Fonamentals

1. **Repositori Lleuger i Col·laboratiu (Text Pur):** El repositori a GitHub només conté text (arxius `.md` i índexs). Les imatges i arxius pesats queden ignorats pel `.gitignore` perquè clonar o sincronitzar el projecte sigui ràpid per a tothom. Cadascú guarda les seves fotos de classe en local.
2. **Unitat Conceptual (No Fragmentació):** Cada nota cobreix un **tema complet** (com ara *Determinants*, *Successions* o *Espais Vectorials*), evitant dividir els apunts per pàgina o per dia de classe.
3. **Fidelitat al Temari Impartit:** Les notes han de reflectir el que realment s'ha fet a classe. No s'han d'afegir teories o seccions de llibres externs que no s'hagin explicat.
4. **Tractament d'Errors o Errates:** Si en passar a net es detecta una relliscada (un signe equivocat, un error de càlcul, un índex canviat o una incoherència lògica), es corregeix per mantenir el rigor, però **s'indica clarament** amb un callout:
   ```markdown
   > [!NOTE] Nota d'esmena
   > Als apunts originals constava ..., però s'ha corregit per ... perquè ...
   ```
5. **Interconnexió:** Ús de wikilinks d'Obsidian (`[[Nom de la Nota]]`) i actualització dels índexs perquè tot estigui connectat.

---

## 2. Esquema de Directoris

```text
Matematiques/
├── Índex.md                        # Índex principal del grau (a l'arrel de l'arca)
├── README.md                       # Documentació i instruccions de clonació
├── GUIA_APUNTS.md                  # Aquesta guia
├── scripts/                        # Utilitats i scripts d'automatització
│   └── generar_llibre.py           # Compilador HTML/PDF (opcions per curs/assignatura)
├── Apunts Fotos/                   # Carpeta local (no es puja a GitHub)
│   ├── registre_fotos.csv          # Seguiment personal de fotos processades
│   └── <NomAssignatura>/           # Fotos locals d'apunts en brut
└── Apunts/                         # Notes organitzades per curs acadèmic
    ├── 1r Curs/
    │   ├── Índex - 1r Curs.md      # MOC del primer curs
    │   └── <Assignatura>/          # ex: Algebra 1, Fonaments 1, etc.
    │       ├── Índex - <Nom>.md    # Índex específic de la matèria
    │       └── <NN>. <Tema>.md     # Temes en Markdown
    └── 2n Curs/
        ├── Índex - 2n Curs.md      # MOC del segon curs
        └── <Assignatura>/          # ex: Analisi Matematica
            ├── Índex - <Nom>.md
            └── <NN>. <Tema>.md
```

---

## 3. Convencions de Format

* **$\LaTeX$:** Fórmules en línia amb `$x \in \mathbb{R}$` i blocs desplegats amb `$$...$$`. Tancar les demostracions amb `\blacksquare`. Conjunts usuals: `\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{K}`.
* **Callouts d'Obsidian:**
  * `> [!IMPORTANT] Teorema / Definició`: Resultats centrals i definicions formals.
  * `> [!NOTE] Proposició / Lema / Nota d'esmena`: Resultats derivats i correcció d'errades.
  * `> [!WARNING] Atenció`: Trampes típiques o casos especials.
  * `> [!TIP] Intuïció`: Interpretacions geomètriques o consells pràctics.
* **Navegació:** Al final de cada nota s'inclouen enllaços a l'`[[Índex]]`, a l'índex del curs (`[[Índex - 1r Curs]]`), a l'índex de l'assignatura, i al tema anterior/següent.

---

## 4. Protocol per Afegir Nous Continguts

Aquest protocol el pot seguir qualsevol persona manualment o bé demanar-lo a una IA. En ambdós casos, cal tenir clar on va el contingut.

1. **Preparar el material en brut (en local):** Guarda les fotos o notes originals a la carpeta local corresponent (ex: `Apunts Fotos/<NomAssignatura>/`).
2. **Decidir la destinació:**
   * *Si és continuació d'un tema:* S'amplia la nota existent (`Apunts/<Curs>/<Assignatura>/<Tema Actual>.md`).
   * *Si comença un tema nou:* Es crea la següent nota (`<NN+1>. <Nom del Nou Tema>.md`) dins de `Apunts/<Curs>/<Assignatura>/`.
3. **Redactar i passar a net:**
   * **Si ho fas manualment:** Escriu el contingut a Obsidian amb el màxim rigor pas a pas, emprant $\LaTeX$ i destacant els teoremes amb callouts. Si veus una errada als apunts originals, corregeix-la i afegeix la *Nota d'esmena*.
   * **Si fas servir una IA:** Dóna-li les fotos i indica-li exactament on van.
     *Exemple de prompt:*
     > *"He afegit noves fotos a `Apunts Fotos/Algebra1/`. Són la continuació del tema `04. Espais Vectorials.md` (1r Curs). Passa-les a net seguint la GUIA_APUNTS.md i actualitza els índexs."*
4. **Actualitzar els índexs:**
   * Afegeix el llistat dels títols dels apartats (en negreta, sense informació extra) a l'índex de l'assignatura (`Índex - <Assignatura>.md`).
   * Assegura't que l'índex del curs (`Índex - <Curs>.md`) i el general (`Índex.md`) tenen la referència al nou tema.
   * *(Opcional en local)* Si portes el control amb `registre_fotos.csv`, marca les fotos com a processades.
