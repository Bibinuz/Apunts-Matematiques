# Guia d'Organització dels Apunts de Matemàtiques

Document normatiu d'estructura, estil i protocol d'incorporació de nous apunts en un entorn col·laboratiu i lleuger.

---

## 1. Principis Fonamentals

1. **Repositori Lleuger i Col·laboratiu (Text Pur):** El repositori Git està pensat per compartir-se entre companys de carrera. Només s'hi sincronitza text pur (fitxers `.md` i índexs). **Totes les imatges (`*.jpg`, `*.png`, etc.) són ignorades per `.gitignore`** per evitar que clonar o actualitzar el repositori sigui pesat.
2. **Unitat Conceptual (No Fragmentació):** Cada nota de Markdown cobreix un **tema o unitat conceptual completa** (no es creen fitxers per pàgina o foto).
3. **Fidelitat Absoluta a les Fotos (100%):** Es transcriu **únicament** el que s'ha impartit a classe. Prohibit afegir temari extern o anticipat de llibres de text.
4. **Correcció d'Errors de Pissarra:** Si es detecta una errada lògica, de signe, d'índexs o aritmètica a la pissarra, es corregeix al text per garantir el rigor matemàtic i s'indica obligatòriament amb el callout:
   ```markdown
   > [!NOTE] Nota de correcció lògica
   > Als apunts originals de pissarra constava ..., però s'ha corregit per ... atès que ...
   ```
5. **Interconnexió:** Ús sistemàtic d'enllaços interns d'Obsidian (`[[Nom de la Nota]]`) i actualització coordinada dels índexs.

---

## 2. Esquema de Directoris

```text
Matematiques/
├── .gitignore                      # Ignora totes les fotos i fitxers pesats
├── GUIA_APUNTS.md                  # Aquesta guia
├── Apunts Fotos/                   # DIPÒSIT LOCAL (ignorat per Git, no es puja a GitHub)
│   ├── registre_fotos.csv          # Registre de seguiment de fotos processades
│   └── <NomAssignatura>/           # Fotos locals de classe de cada col·laborador
└── Apunts/                         # CONTINGUT SINCRONITZAT (text Markdown)
    ├── Índex.md                    # Hub d'accés principal
    ├── Índex - <Assignatura>.md    # Índex temàtic per assignatura
    └── <NomAssignatura>/           # Carpetes de les matèries
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

## 4. Protocol d'Incorporació de Nous Apunts

Com que les imatges són locals a cada màquina, **és l'usuari qui indica a la petició la destinació dels apunts**:

1. **Desar les imatges en local:** Guardar les fotos a la carpeta local `Apunts Fotos/<NomAssignatura>/`.
2. **Indicar la destinació a la petició:** Especificar clarament en el prompt a quina nota han d'anar els nous apunts:
   * *Continuació de tema:* Indicar la nota existent a ampliar (ex: *"ampliar la nota `04. Espais Vectorials.md`"*).
   * *Nou tema:* Indicar que és un tema nou (ex: *"crear el nou tema `05. Subespais Vectorials.md`"*).
   * *Exemple de prompt:*
     > *"He afegit noves fotos a `Apunts Fotos/Algebra1/`. Són la continuació del tema `04. Espais Vectorials.md`. Transcriu-les seguint la GUIA_APUNTS.md i actualitza els índexs."*
3. **Transcripció i Integració:** Transcriure amb rigor en $\LaTeX$, fidelitat 100% a les imatges i callouts de correcció si cal.
4. **Actualitzar índexs i registre:**
   * Actualitzar el resum del tema a `Índex - <Assignatura>.md` i `Índex.md`.
   * Registrar les fotos al fitxer de seguiment `Apunts Fotos/registre_fotos.csv`.
