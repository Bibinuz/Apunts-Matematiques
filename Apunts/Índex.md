# Grau de Matemàtiques — Índex General

Benvingut/da al **Repositori Centralitzat d'Apunts del Grau de Matemàtiques**. Aquest espai conté tots els apunts teòrics, teoremes, lemes, demostracions rigoroses i exemples extrets i transcrits de les classes presencials.

---

## Assignatures i Blocs Temàtics

```
Apunts/
├── Índex.md (aquest fitxer)
├── Índex - Àlgebra 1.md
├── Índex - Fonaments 1.md
├── Índex - Funcions 1.md
├── Índex - Mecànica Clàssica.md
├── Algebra 1/
├── Fonaments 1/
├── Funcions 1/
└── Mecanica Classica/
```

---

### 1. [[Índex - Àlgebra 1|Àlgebra Lineal 1]]
Assignatura centrada en l'estudi de sistemes d'equacions lineals, àlgebra matricial, espais vectorials i aplicacions multilineals.
- **Tema 1:** [[01. Sistemes Lineals, Matrius i Operacions Elementals]]
  - *Sistemes lineals, matrius ampliades, operacions elementals per files/columnes, matrius elementals ($E_{ij}, D_i, P_{ij}$), forma esglaonada i reduïda (RREF), algorisme de Gauss i teorema de reducció per inducció.*
- **Tema 2:** [[02. PAQ-Reducció, Rang i Teorema de Rouché-Frobenius]]
  - *Equivalència de matrius, PAQ-reducció ($PAQ = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$), rang per files i per columnes, criteris d'invertibilitat, càlcul d'inversa per Gauss-Jordan i Teorema de Rouché-Frobenius (SCD, SCI, SI).*
- **Tema 3:** [[03. Determinants]]
  - *Interpretació geomètrica d'àrees i volums orientats, definició axiomàtica multilineal i alternada, deducció formal en $2 \times 2$, determinants d'elementals, Teorema de Binet-Cauchy ($\det(AB)=\det(A)\det(B)$) amb prova en 3 passos, criteri d'invertibilitat, inversa unilateral, teorema de la transposada, desenvolupament de Laplace, el grup simètric $S_n$, transposicions i signe, fórmula explícita de Leibniz i demostració completa d'existència i unicitat.*
- **Tema 4:** [[04. Espais Vectorials]]
  - *Estructura algebraica de cos $(\mathbb{K}, +, \cdot)$ (axiomes i exemples: $\mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}, \mathbb{Q}(\sqrt{2})$), motivació geomètrica de $\mathbb{R}^n$, validesa de la teoria matricial sobre cossos arbitraris $\mathbb{K}$, definició formal d'espai vectorial (8 axiomes: grup abelià per a $(E, +)$ i compatibilitat d'escalars), i exemples canònics: l'espai nul $\{\vec{0}\}$, $\mathbb{K}^n$, matrius $\mathcal{M}_{m \times n}(\mathbb{K})$, polinomis $\mathbb{K}[x]$ i polinomis de grau fitat $\mathbb{K}_n[x]$.*

---

### 2. [[Índex - Fonaments 1|Fonaments de les Matemàtiques 1]]
Assignatura que estableix el llenguatge formal, la lògica, els mètodes de demostració i les estructures algebraico-conjuntistes bàsiques.
- **Tema 1:** [[01. Resolució d'Equacions i Mètodes de Demostració]]
  - *Concepte d'equació i conjunt de solucions, mètode de doble inclusió, deducció per completació de quadrats de la fórmula quadràtica, context històric (Cardano, Tartaglia, Abel, Galois) i demostració per reducció a l'absurd de la irracionalitat de $\sqrt{2}$.*
- **Tema 2:** [[02. Teoria de Conjunts i Construccions Fonamentals]]
  - *Infinit potencial vs en acte, definició de Dedekind de conjunt infinit, prova que $\mathbb{N}$ és infinit, axiomes de Peano, principi d'inducció matemàtica, operacions de conjunts, De Morgan, conjunt de les parts $\mathcal{P}(A)$, producte cartesià i la seva Propietat Universal.*
- **Tema 3:** [[03. Relacions Binàries, Equivalència i Ordre]]
  - *Definició formal de relació binària, grafs i matrius booleanes, propietats (reflexiva, simètrica, antisimètrica, transitiva), relacions d'ordre (posets), divisibilitat a $\mathbb{N}^*$, elements notables (minimal, maximal, mínim, màxim), ordres finits i diagrames de Hasse, ordres densos i Teorema de Cantor de $(\mathbb{Q}, \le)$, Corol·lari de classificació en 4 ordres lineals densos segons extrems, relacions d'equivalència (R, S, T), classes d'equivalència $\bar{a}$, representants, conjunt quocient $E/R$, projecció canònica $\pi$ i Teorema de la Partició.*

---

### 3. [[Índex - Funcions 1|Funcions d'una Variable 1 (Càlcul / Anàlisi 1)]]
Assignatura dedicada a l'anàlisi matemàtica rigorosa a la recta real $\mathbb{R}$.
- **Tema 1:** [[01. Els Nombres Reals i Propietats Fonamentals]]
  - *Cossos ordenats, cotes, suprem i ínfim, insuficiència de $\mathbb{Q}$ ($x^2 < 2$), Axioma de Completesa de $\mathbb{R}$, caracterització per $\varepsilon$, propietat arquimediana, part sencera $[x]$, densitat de $\mathbb{Q}$ i dels irracionals $\mathbb{R} \setminus \mathbb{Q}$, operacions entre conjunts de nombres i valor absolut amb desigualtats triangulars.*
- **Tema 2:** [[02. Cardinalitat i Numerabilitat]]
  - *Desenvolupament decimal (periòdic vs no periòdic) i unicitat, aplicacions injectives/bijectives, definició de numerabilitat ($\aleph_0$), bijecció de $\mathbb{Z}$, numerabilitat de subconjunts i productes cartesians, demostracions que $\mathbb{Q}$ és numerable, i l'argument diagonal de Cantor provant que $\mathbb{R}$ no és numerable.*
- **Tema 3:** [[03. Successions de Nombres Reals]]
  - *Concepte de successió real, successions acotades i monòtones, definició formal de límit ($\varepsilon$-$n_0$), càlcul explícit de llindars, unicitat del límit, acotació de convergents, preservació de desigualtats febles, àlgebra de límits amb proves detallades per $\varepsilon$, Teorema de la Convergència Monòtona, formes indeterminades, Teorema de l'Encaix (Sandvitx), producte d'infinitèsim per acotada, límits infinits i escales fonamentals de creixement mitjançant el Binomi de Newton ($\ln n \ll n^\alpha \ll x^n \ll n! \ll n^n$), i criteris avançats de càlcul: Stolz-Cesàro, arrel de Cauchy, quocient de d'Alembert i criteri quocient-arrel.*

---

### 4. [[Índex - Mecànica Clàssica|Mecànica Clàssica]]
Assignatura de física matemàtica orientada a l'estudi del moviment de sistemes materials, cinemàtica, dinàmica newtoniana i principis de conservació.
- **Tema 1:** [[01. Cinemàtica en 2D i 3D]]
  - *Marc vectorial a l'espai euclidià, vector posició $\vec{r}(t)$, vector desplaçament $\vec{AB}$, àlgebra de vectors, descomposició en base ortonormal $\{\hat{i}, \hat{j}, \hat{k}\}$, vector velocitat instantània $\vec{v} = \frac{d\vec{r}}{dt}$ i tangència, vector acceleració instantània $\vec{a} = \frac{d^2\vec{r}}{dt^2}$, i estudi complet del tir parabòlic (llançament de projectils en 2D sense fricció: equacions horàries, equació de la trajectòria, alçada màxima, temps de vol i abast màxim).*

---

## Pautes de Consulta Ràpida

> [!TIP] Navegació a Obsidian
> - Prem `Ctrl + O` (o `Cmd + O` a macOS) per obrir qualsevol nota directament escrivint el seu títol.
> - Utilitza la vista de graf (**Graph View**) per veure com interactuen els teoremes i assignatures entre si.
> - Per afegir nous apunts o continuar ampliant el contingut, consulta el document guia situat a l'arrel: `GUIA_APUNTS.md`.
