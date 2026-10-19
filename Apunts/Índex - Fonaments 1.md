# Índex — Fonaments de les Matemàtiques 1

Benvingut/da al mòdul de **Fonaments 1**. Aquest bloc estableix les bases del raonament matemàtic rigorós: mètodes de demostració, teoria de conjunts formal, construccions canòniques i la teoria de relacions binàries (equivalència i ordre).

---

## Mapa de Continguts (MOC)

### 1. [[01. Resolució d'Equacions i Mètodes de Demostració]]
- **Concepte formal d'equació:** Conjunt de solucions $S = \{x \in E : f(x) = 0\}$.
- **Mètode de doble inclusió:** Condició necessària ($S \subseteq S_0$) i condició suficient ($S_0 \subseteq S$) per evitar solucions estranyes.
- **Equació quadràtica:** Deducció rigorosa de la fórmula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ mitjançant la tècnica de completació de quadrats. Anàlisi del discriminant $\Delta$.
- **Perspectiva històrica:** Resolució per radicals de les equacions cúbica (Cardano-Tartaglia) i quàrtica (Ferrari), i impossibilitat per a grau $\ge 5$ (Teorema d'Abel-Ruffini i Teoria de Galois).
- **Mètode de reducció a l'absurd:** Estructura lògica. Demostració clàssica completa de la irracionalitat de $\sqrt{2}$ ($\sqrt{2} \notin \mathbb{Q}$).

### 2. [[02. Teoria de Conjunts i Construccions Fonamentals]]
- **La noció d'infinit:** Infinit potencial (Aristòtil) versus infinit en acte (Cantor).
- **Definició de Dedekind de conjunt infinit:** Un conjunt és infinit si és equipotent a un subconjunt propi. Demostració que $\mathbb{N}$ és infinit mitjançant l'aplicació successor $s(n) = n+1$.
- **Axiomes de Peano i Inducció:** Formulació dels 5 axiomes de Peano i estructura de les demostracions per inducció matemàtica (cas base, pas inductiu, conclusió).
- **Àlgebra de conjunts:** Formes de definició (enumeració, extensionalitat/especificació, construcció), inclusió, unicitat del conjunt buit ($\emptyset$), operacions bàsiques ($\cup, \cap, \setminus, \complement$), caracterització extremal, lleis de De Morgan, conjunt potència $\mathcal{P}(A)$ ($|\mathcal{P}(A)| = 2^n$) i teorema de monotonia.
- **Producte cartesià:** Construcció de Kuratowski de parells ordenats $(a, b)$, definició de $E \times F$, projeccions canòniques $\pi_1, \pi_2$, formulació categòrica de la Propietat Universal del Producte Cartesià i generalització a famílies arbitràries amb l'Axioma de l'Elecció.

### 3. [[03. Relacions Binàries, Equivalència i Ordre]]
- **Definició de relació binària:** Graf $\Gamma \subseteq A \times B$ i relacions sobre un conjunt $A$. Representacions mitjançant dígrafs, diagrames sagitals i matrius d'adjacència booleanes.
- **Propietats sobre un conjunt:** Reflexivitat, irreflexivitat, simetria, antisimetria (formulació estàndard i contrarecíproca) i transitivitat.
- **Relacions d'ordre (Posets):** Ordre parcial, ordre total i comparabilitat. Estudi complet de la relació de divisibilitat a $\mathbb{N}^*$ (proves de reflexivitat, antisimetria via $lk = 1$, i transitivitat).
- **Elements notables:** Definicions formals de minimal, maximal, mínim (primer element) i màxim (últim element). Diferenciació entre mínim i minimal; estudi dels nombres primers a $\mathbb{N} \setminus \{0, 1\}$ (múltiples minimals, sense mínim) vs $\mathbb{N}^*$ (mínim $1$).
- **Teoremes d'existència i unicitat:** Demostració que el mínim i màxim són únics; existència d'almenys un minimal i un maximal en tot poset finit no buit (demostració per cadenes). Diagrames de Hasse.
- **Teorema de Cantor de caracterització de $(\mathbb{Q}, \le)$:** Definicions d'ordre dens, sense extrems i d'isomorfisme de posets. Demostració completa del teorema d'isomorfisme d'ordres lineals numerables densos sense extrems mitjançant el mètode d'anada i tornada (*Back-and-Forth*).

---
*Enllaços de navegació:*
- [[Índex|← Tornar a l'Índex Principal]]
