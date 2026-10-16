# Índex — Funcions d'una Variable 1

Benvingut/da al mòdul de **Funcions 1** (Càlcul / Anàlisi Matemàtica 1). Aquest bloc estableix els fonaments de l'anàlisi real: la construcció i propietats dels nombres reals, cardinalitat i teoria de la numerabilitat de Cantor, i la teoria de successions i convergència.

---

## Mapa de Continguts (MOC)

### 1. [[01. Els Nombres Reals i Propietats Fonamentals]]
- **El cos ordenat $\mathbb{R}$:** Axiomes algebraics i d'ordre.
- **Cotes, suprem i ínfim:** Definicions formals i demostració de la unicitat del suprem.
- **Insuficiència de $\mathbb{Q}$:** Demostració que $A = \{x \in \mathbb{Q} : x > 0, x^2 < 2\}$ no té suprem a $\mathbb{Q}$.
- **Axioma de Completesa:** Existència de la cota superior mínima a $\mathbb{R}$. Caracterització per $\varepsilon$ del suprem i ínfim (existència d'elements a $(\alpha - \varepsilon, \alpha]$).
- **Propietat Arquimediana:** No acotació de $\mathbb{N}$ a $\mathbb{R}$ (amb demostració) i el lema $\frac{1}{n} < y - x$.
- **Funció part sencera ($[x]$):** Existència i unicitat.
- **Teoremes de densitat:** Demostració completa de la densitat de $\mathbb{Q}$ a $\mathbb{R}$ mitjançant $[nx]$, i densitat dels irracionals $\mathbb{R} \setminus \mathbb{Q}$ a $\mathbb{R}$ mitjançant $\sqrt{2}$.
- **Àlgebra de racionals i irracionals:** Clausura de $\mathbb{Q}$, operacions mixtes i casos indeterminats d'irracionals.
- **Valor absolut:** Definició com $\max\{x, -x\}$, les 7 propietats fonamentals, demostració de la desigualtat triangular i desigualtat triangular inversa.

### 2. [[02. Cardinalitat i Numerabilitat]]
- **Desenvolupament decimal:** Decimals periòdics versus no periòdics, i conveni d'unicitat per evitar cues de 9 ($0.999\dots = 1$).
- **Equipotència:** Bijeccions entre conjunts.
- **Conjunts numerables:** Definició formal ($|A| = |\mathbb{N}| = \aleph_0$). Demostració explícita de la numerabilitat de $\mathbb{Z}$ via bijecció intercalada.
- **Proposicions clau:** Subconjunts infinits de numerables són numerables; equivalència amb l'existència d'injecció cap a $\mathbb{N}$; numerabilitat del producte cartesià $A \times B$ demostrada via factorització en nombres primers ($2^{i(a)} 3^{j(b)}$).
- **Teorema de la numerabilitat de $\mathbb{Q}$:** Prova per descomposició en primers i via l'ordenació diagonal en ziga-zaga de Cantor per a $\mathbb{Q}^+`.
- **Incomptabilitat de $\mathbb{R}$:** Demostració mestra per l'**argument diagonal de Cantor** que $(0, 1)$ no és numerable, concloent que $|\mathbb{R}| = \mathfrak{c} = 2^{\aleph_0} > \aleph_0$.

### 3. [[03. Successions de Nombres Reals]]
- **Concepte de successió:** Aplicació $a: \mathbb{N} \to \mathbb{R}$.
- **Acotació i monotonia:** Cotes superiors, inferiors, creixement i decreixement estricte.
- **Definició formal de límit ($\varepsilon$-$n_0$):** Interpretació dinàmica i geomètrica d'entorns d'$\varepsilon$.
- **Demostracions pràctiques per definició:**
  - $\lim_{n \to \infty} \frac{1}{n} = 0$ amb $n_0 = [1/\varepsilon] + 1$.
  - $\lim_{n \to \infty} \frac{n+3}{n+2} = 1$ amb fites analítiques.
  - Anàlisi de la divergència d'$a_n = (-1)^n$.
- **Teorema d'unicitat del límit:** Demostració per reducció a l'absurd amb $\varepsilon = \frac{|L_1 - L_2|}{3}$ i desigualtat triangular.
- **Proposició Fonamental de Convergència i Acotació:**
  - Tota successió convergent és acotada: Demostració formal amb conjunt finit $M = \{a_1, \dots, a_{n_0}, L - 1/2, L + 1/2\}$ i els seus extrems $\max(M)$ i $\min(M)$.
  - El recíproc és fals: Contraexemple d'$a_n = (-1)^n$ (acotada però no convergent).
- **Preservació de desigualtats febles pel límit:** Demostració per reducció a l'absurd amb $\varepsilon = \frac{a - K}{2}$. Pas de desigualtats estrictes a febles al límit.
- **Àlgebra de límits:** Demostracions rigoroses amb $\varepsilon$: suma ($\varepsilon/2$), producte (terme creuat $a_n b$ i fitació de convergents), i invers (lema $|b_n| > |b|/2$).
- **Teorema de la Convergència Monòtona:** Tota successió creixent i acotada superiorment convergeix a $\alpha = \sup A$ (demostració rigorosa per completesa i caracterització del suprem). Cas decreixent amb $\inf A$.
- **Càlcul d'indeterminacions:** Resolució de la indeterminació $\infty - \infty$ mitjançant multiplicació i divisió pel conjugat ($\lim (\sqrt{n^2+1}-n) = 0$).

---
*Enllaços de navegació:*
- [[Índex|← Tornar a l'Índex Principal]]
