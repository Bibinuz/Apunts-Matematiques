# Guia d'Organització dels Apunts de Matemàtiques

Aquest document estableix la filosofia, estructura, convencions de format i el protocol de treball per continuar ampliant els apunts a mesura que s'afegeixin noves fotografies d'apunts presos a classe.

---

## 1. Filosofia dels Apunts

1. **Centralització:** Tot el grau de matemàtiques es troba recollit en un únic espai d'apunts d'Obsidian.
2. **Cohesió i No Fragmentació:** Els apunts **no** s'han de dividir foto a foto ni pàgina a pàgina. Cada nota de Markdown ha de correspondre a un **tema o unitat conceptual completa** (per exemple: *Sistemes Lineals i Operacions Elementals*, *Determinants*, *Successions de Nombres Reals*). D'aquesta manera es manté una lectura fluïda, interconnectada i acadèmica.
3. **Rigor Matemàtic i Transcripció Fidel:** Totes les definicions, lemes, teoremes, proposicions i demostracions escrites a mà han de quedar transcrites amb el màxim rigor formal, utilitzant notació $\LaTeX$ estàndard i explicacions clares pas a pas.
4. **Interconnexió:** Ús de wikilinks d'Obsidian (`[[Nom de la Nota]]`) per interconnectar conceptes entre diferents temes i assignatures.

---

## 2. Estructura de Directoris

L'organització del directori arrel del projecte és la següent:

```text
/home/bibinuz/Documents/Matematiques/
│
├── GUIA_APUNTS.md                     # Aquesta guia de referència i protocol
│
├── Apunts Fotos/                      # Dipòsit de fotografies originals (entrades)
│   ├── registre_fotos.csv             # Registre de seguiment (estat de processament, nota destí, data)
│   ├── Algebra1/                      # Imatges d'Àlgebra Lineal 1
│   ├── Fonaments1/                    # Imatges de Fonaments de les Matemàtiques 1
│   ├── Funcions1/                     # Imatges de Funcions d'una Variable 1
│   ├── MecanicaClassica/              # Imatges de Mecànica Clàssica
│   └── <Altres Assignatures>/        # Futures assignatures (ex: Geometria1, etc.)
│
└── Apunts/                            # Carpeta principal de notes processades en Markdown (.md)
    ├── Índex.md                       # PUNT D'ENTRADA PRINCIPAL (Hub central de tots els apunts)
    ├── Índex - Àlgebra 1.md           # Índex específic d'Àlgebra 1
    ├── Índex - Fonaments 1.md         # Índex específic de Fonaments 1
    ├── Índex - Funcions 1.md          # Índex específic de Funcions 1
    ├── Índex - Mecànica Clàssica.md   # Índex específic de Mecànica Clàssica
    │
    ├── Algebra 1/                     # Notes temàtiques d'Àlgebra 1
    │   ├── 01. Sistemes Lineals, Matrius i Operacions Elementals.md
    │   ├── 02. PAQ-Reducció, Rang i Teorema de Rouché-Frobenius.md
    │   └── 03. Determinants.md
    │
    ├── Fonaments 1/                   # Notes temàtiques de Fonaments 1
    │   ├── 01. Resolució d'Equacions i Mètodes de Demostració.md
    │   ├── 02. Teoria de Conjunts i Construccions Fonamentals.md
    │   └── 03. Relacions Binàries, Equivalència i Ordre.md
    │
    ├── Funcions 1/                    # Notes temàtiques de Funcions 1
    │   ├── 01. Els Nombres Reals i Propietats Fonamentals.md
    │   ├── 02. Cardinalitat i Numerabilitat.md
    │   └── 03. Successions de Nombres Reals.md
    │
    └── Mecanica Classica/             # Notes temàtiques de Mecànica Clàssica
        └── 01. Cinemàtica en 2D i 3D.md
```

> [!NOTE] Criteri per als fitxers d'Índex
> Els fitxers d'índex (`Índex.md` i els índexs per assignatura `Índex - <Assignatura>.md`) resideixen directament a l'arrel de la carpeta `Apunts/`. Això permet tenir els punts d'accés separats de les subcarpetes temàtiques, facilitant una cerca ràpida a Obsidian.

---

## 3. Convencions d'Estil i Format Matemàtic

### Expressió Matemàtica en $\LaTeX$
- **Fórmules en línia (inline):** Utilitzar un sol símbol de dòlar: `$x \in \mathbb{R}$`, `$Ax = b$`, `$\lim_{n \to \infty} a_n = L$`.
- **Fórmules desplegades (display):** Utilitzar doble símbol de dòlar en blocs independents:
  ```latex
  $$\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det(A_{ij})$$
  ```
- **Conjunts numèrics estàndard:** Utilitzar `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{Q}`, `\mathbb{R}`, `\mathbb{C}`, `\mathbb{K}`.
- **Espais matricials i operadors:** Utilitzar `\mathcal{M}_{m \times n}(\mathbb{K})`, `\operatorname{rang}(A)`, `\operatorname{rref}(A)`, `\operatorname{GL}_n(\mathbb{K})`, `\operatorname{Nuc}(A)`.
- **Final de demostració:** Finalitzar cada prova amb el quadrat negre `\blacksquare`.

### Ús de Callouts d'Obsidian
Per destacar la jerarquia teòrica, s'utilitzen els callouts estàndard de GitHub / Obsidian:
- `> [!IMPORTANT] Teorema / Definició`: Per a definicions principals, axiomes i teoremes rellevants.
- `> [!NOTE] Proposició / Lema`: Per a proposicions secundàries, lemes o corol·laris.
- `> [!WARNING] Atenció / Cas Particular`: Per a casos concrets que solen induir a errors o convenis especials (com l'exclusió de cues de 9s en decimals).
- `> [!TIP] Idea Clau / Intuïció Geomètrica`: Per a interpretacions gràfiques o mètodes de resolució pràctics.

### Enllaços de Navegació
Al final de cada nota, incloure sempre una secció d'enllaços relacionats:
```markdown
---
*Enllaços relacionats:*
- [[Índex|Tornar a l'Índex Principal]]
- [[Tema Anterior]]
- [[Tema Següent]]
```

---

## 4. Protocol per Afegir Noves Fotos

> [!IMPORTANT] No esborris mai les fotografies anteriors!
> Les fotografies són el material de referència primari (la font original de la pissarra). Conservar-les et permet contrastar demostracions, notacions del professor o esquemes visuals en el futur.
> El seguiment de quines imatges estan ja incorporades es gestiona de forma centralitzada a l'arxiu `Apunts Fotos/registre_fotos.csv`. No cal esborrar cap foto prèvia per afegir-ne de noves; simplement afegeix les noves fotos a la carpeta de l'assignatura corresponent.

Quan assisteixis a noves classes i facis fotografies de la pissarra o dels teus apunts en paper, segueix aquest procediment pas a pas:

### Pas 1: Desar les Imatges
1. Desa les fotografies directament a la carpeta corresponent dins de `Apunts Fotos/`:
   - Si és una assignatura existent: ex. `Apunts Fotos/Algebra1/nova_foto1.jpg`.
   - Si és una assignatura nova: crea la subcarpeta, per exemple `Apunts Fotos/Geometria1/`.
2. Assegura't que les fotos estiguin orientades correctament i que la resolució permeti llegir els subíndexs i superíndexs matemàtics.

### Pas 2: Decisió d'Agrupació (Evitar Fragmentació)
Quan es transcriguin les noves fotos, avalua:
- **És continuació d'un tema ja existent?** (Per exemple, si a Funcions 1 s'explica la convergència monòtona o subsuccessions).
  - *Acció:* Ampliar la nota existent (`03. Successions de Nombres Reals.md`) afegint les noves seccions.
- **És un nou tema o bloc didàctic?** (Per exemple, càlcul de límits i continuïtat de funcions).
  - *Acció:* Crear una nova nota amb la numeració correlativa (ex: `04. Límits de Funcions i Continuïtat.md`).

### Pas 3: Transcripció i Integració
1. Llegir i transcriure el contingut manualment o sol·licitar a l'assistent:
   > *"He afegit noves fotos a `Apunts Fotos/<Assignatura>`. Llegeix-les seguint la `GUIA_APUNTS.md`, integra el contingut ampliant la nota corresponent o creant el següent tema sense fragmentar excessivament, i actualitza els índexs."*
2. Verificar que totes les fórmules estiguin en $\LaTeX$ i que les demostracions tinguin tots els passos lògics complets.
3. Actualitzar:
   - L'índex específic de l'assignatura (`Apunts/Índex - <Assignatura>.md`).
   - L'índex general (`Apunts/Índex.md`).

### Pas 4: Actualització del Registre (`registre_fotos.csv`)
Actualitzar l'arxiu `Apunts Fotos/registre_fotos.csv`:
- Marcar l'estat com a `Processat`.
- Indicar el fitxer de destí (`Nota_Desti`), la data de processament i una breu descripció dels conceptes transcrits.
