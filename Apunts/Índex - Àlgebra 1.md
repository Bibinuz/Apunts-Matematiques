# Índex — Àlgebra Lineal 1

Benvingut/da al mòdul d'**Àlgebra 1**. Aquest bloc cobreix la teoria fonamental de sistemes lineals, àlgebra matricial, reducció per files i columnes, rang, invertibilitat, resolució mitjançant el Teorema de Rouché-Frobenius i la teoria axiomàtica dels determinants.

---

## Mapa de Continguts (MOC)

### 1. [[01. Sistemes Lineals, Matrius i Operacions Elementals]]
- **Sistemes d'equacions lineals:** Formulació general, matriu de coeficients $A$, vector de termes independents $b$, i matriu ampliada $(A \mid b)$.
- **Operacions elementals per files:** Permutació ($F_i \leftrightarrow F_j$), dilatació ($F_i \leftarrow \alpha F_i$), transvecció ($F_i \leftarrow F_i + \lambda F_j$).
- **Matrius elementals:** Matrius $E_{ij}, D_i(\alpha), P_{ij}(\lambda)$, multiplicació per l'esquerra (files) i per la dreta (columnes), i les seves inverses.
- **Forma esglaonada i esglaonada reduïda (RREF):** Definició de pivots, condicions formals d'esglaonament.
- **Teorema de reducció:** Existència i unicitat de la forma esglaonada reduïda. Demostració completa per inducció sobre el nombre de files $m$.
- **Resolució de sistemes:** Classificació entre variables pivot (bàsiques) i variables lliures (secundàries).

### 2. [[02. PAQ-Reducció, Rang i Teorema de Rouché-Frobenius]]
- **Equivalència de matrius:** Definició $B = PAQ$ amb $P, Q$ invertibles.
- **Teorema de la PAQ-Reducció:** Descomposició canònica $PAQ = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$. Algorisme pràctic per files i columnes.
- **Rang d'una matriu:** Rang per files ($\operatorname{rang}_f$), rang per columnes ($\operatorname{rang}_c$), i el Teorema fonamental $\operatorname{rang}_f(A) = \operatorname{rang}_c(A) = \operatorname{rang}(A^t)$. Propietats i cotes del rang.
- **Criteris d'invertibilitat:** Les 9 caracteritzacions equivalents d'una matriu invertible a $\mathcal{M}_n(\mathbb{K})$. Càlcul d'inverses per Gauss-Jordan $(A \mid I) \sim (I \mid A^{-1})$.
- **Teorema de Rouché-Frobenius:** Criteri de compatibilitat ($\operatorname{rang}(A) = \operatorname{rang}(A \mid b)$), classificació en SCD ($r = n$), SCI ($r < n$, amb $n - r$ graus de llibertat) i SI. Estructura afí del conjunt de solucions $S = x_p + \operatorname{Nuc}(A)$.

### 3. [[03. Determinants]]
- **Motivació geomètrica:** Àrea orientada d'un paral·lelogram a $\mathbb{R}^2$, volums orientats a $\mathbb{R}^3$ i hipervolums a $\mathbb{R}^n$.
- **Definició axiomàtica:** L'única funció $\det: \mathcal{M}_n(\mathbb{K}) \to \mathbb{K}$ multilineal, alternada i normalitzada ($\det(I_n) = 1$). Deducció formal unívoca de $\det \begin{pmatrix} a & c \\ b & d \end{pmatrix} = ad - bc$.
- **Determinant de matrius elementals:** Dilatació ($\det(D) = \lambda$), permutació ($\det(P) = -1$) i transvecció ($\det(E) = 1$).
- **Teorema de Binet-Cauchy ($\det(AB) = \det(A)\det(B)$):** Demostració completa en tres passos (Cas 1 elemental, Cas 2 invertible per inducció, Cas 3 no invertible amb reducció per columnes).
- **Corol·laris i aplicacions:** Criteri d'invertibilitat $A \in \operatorname{GL}_n(\mathbb{K}) \iff \det(A) \neq 0$, $\det(A^{-1}) = (\det(A))^{-1}$, inversa unilateral ($AB = I_n \implies BA = I_n$) i teorema de la transposada $\det(A^t) = \det(A)$.
- **Mètodes pràctics de càlcul:** Càlcul per a ordres 2 i 3 (Regla de Sarrus), triangulació per eliminació gaussiana ($O(n^3)$), desenvolupament per adjunts (Fórmula de Laplace), i expressió explícita de $A^{-1}$ mitjançant la matriu de cofactors.
- **Existència i unicitat (Fórmula de Leibniz):** Permutacions, grup simètric $S_n$, generació per transposicions (demostració per inducció), paritat i signatura $\varepsilon(\sigma) = (-1)^k$, homomorfisme $\varepsilon(\sigma \tau) = \varepsilon(\sigma)\varepsilon(\tau)$, grup alternat $A_n$ ($|A_n| = n!/2$), expressió explícita $\det(A) = \sum_{\sigma \in S_n} \varepsilon(\sigma) a_{\sigma(1), 1} \cdots a_{\sigma(n), n}$, i demostració completa dels 3 axiomes i unicitat.

### 4. [[04. Espais Vectorials]]
- **Estructura algebraica de cos:** Definició axiomàtica d'un cos $(\mathbb{K}, +, \cdot)$ (grup abelià per la suma, grup abelià per als elements no nuls pel producte, distributivitat i $0 \neq 1$).
- **Exemples de cossos:** Cossos infinits estàndard ($\mathbb{Q}, \mathbb{R}, \mathbb{C}$), el cos finit de dos elements $\mathbb{Z}/2\mathbb{Z} = \mathbb{F}_2$ (amb taules de Cayley i característica 2: $1 + 1 = 0$), i l'extensió quadràtica $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ amb demostració de la invertibilitat per racionalització.
- **Definició axiomàtica d'espai vectorial:** Conjunt de vectors $V$ amb suma interna $(V, +)$ (grup abelià) i acció externa d'escalars $\cdot: \mathbb{K} \times V \to V$ que satisfà els 4 axiomes de compatibilitat lineal.

---
*Enllaços de navegació:*
- [[Índex|← Tornar a l'Índex Principal]]
