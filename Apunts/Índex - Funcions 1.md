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
- **Formes indeterminades i Teorema de l'Encaix:** Les 7 formes indeterminades. Demostració rigorosa ($\varepsilon$-$n_0$) de la Regla del Sandvitx i resolució de successions oscil·lants com $b_n = \frac{1 + \sin^2 n + \sin n \cos n}{n} \to 0$.
- **Producte d'un infinitèsim per una successió acotada:** Demostració formal $\varepsilon$-$n_0$ que $\lim a_n = 0 \land |b_n| \le M \implies \lim (a_n b_n) = 0$. Exemples: $\lim \frac{\sin n}{\sqrt{n}} = 0$ i $\lim \frac{1 \cdot 3 \cdots (2n-1)}{(2n)^n} = 0$.
- **Límits infinits i Escala de Creixement via Binomi de Newton:** Definicions formals de divergència a $\pm\infty$. Demostracions completes mitjançant el binomi de Newton de $\lim \frac{1}{n^p} = 0$, $\lim \sqrt[n]{p} = 1$, $\lim \sqrt[n]{n} = 1$, $\lim \frac{n^\alpha}{x^n} = 0$, $\lim x^n = 0$ ($|x| < 1$), $\lim \frac{n!}{n^n} = 0$ i $\lim \frac{x^n}{n!} = 0$. Jerarquia fonamental de creixement: $\ln n \ll n^\alpha \ll x^n \ll n! \ll n^n$.
- **Criteris Avançats per al Càlcul de Límits:**
  - **Criteri de Stolz-Cesàro:** Enunciat per a formes $\infty/\infty$ i $0/0$ amb denominador monòton. Càlcul de $\lim \frac{\ln n}{n} = 0$ i mitjana harmònica. Corol·laris de mitjanes aritmètica i geomètrica.
  - **Criteri de l'arrel de Cauchy:** Condicions de convergència ($L < 1 \implies 0, L > 1 \implies \infty$) i aplicació a la indeterminació $0^\infty$ en $\lim (\sqrt[n]{n} - 1)^n = 0$.
  - **Criteri del quocient de d'Alembert:** Aplicació a $\lim \frac{n!}{n^n} = 0$ (terme $(1 + 1/n)^n \to e$), $\lim \frac{x^n}{n!} = 0$ i $\lim \frac{2^{n^2}}{n!} = +\infty$.
  - **Criteri quocient-arrel:** Teorema $\lim \frac{a_{n+1}}{a_n} = \ell \implies \lim \sqrt[n]{a_n} = \ell$ i la seva aplicació a la divergència de $\lim \sqrt[n]{n!} = +\infty$.

---
*Enllaços de navegació:*
- [[Índex|← Tornar a l'Índex Principal]]
