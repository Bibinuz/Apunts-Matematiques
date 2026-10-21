# Apunts del Grau de Matemàtiques — UAB

Aquest repositori recull els apunts i materials d'estudi per al **Grau en Matemàtiques a la Universitat Autònoma de Barcelona (UAB)**. 

El contingut prové d'apunts presos a classe, passats a net (de forma manual o amb l'assistència d'IA) i redactats íntegrament en català amb el màxim rigor formal. Està estructurat en unitats temàtiques completes seguint el pla docent de la facultat, i optimitzat com a **arca d'Obsidian** (o qualsevol editor de Markdown amb suport per a $\LaTeX$) per a una navegació interconnectada i fluïda.

---

## Instal·lació i Sincronització

Pots descarregar i sincronitzar els apunts fàcilment, tant si estàs acostumat/da a la terminal com si prefereixes una interfície gràfica visual:

### Opció A: Windows (Mètode visual amb GitHub Desktop — Recomanat si no uses terminal)

No cal saber fer servir la terminal ni comandes complexes de Git:

1. **Instal·la GitHub Desktop:** Descarrega'l gratuïtament des de [desktop.github.com](https://desktop.github.com/).
2. **Clona el projecte:**
   - Obre GitHub Desktop i ves al menú superior: `File` > `Clone repository...`.
   - Selecciona la pestanya **URL** i enganxa l'enllaç del repositori:
     ```text
     https://github.com/Bibinuz/Apunts-Matematiques.git
     ```
   - Tria la carpeta del teu ordinador on vols desar els apunts i fes clic a **Clone**.
3. **Com rebre les actualitzacions:** Cada vegada que algú afegeixi temes nous, només has d'obrir GitHub Desktop i fer clic al botó superior **Fetch origin** (o **Pull origin**) per descarregar les novetats amb un sol clic.

---

### Opció B: Linux / macOS (o via Terminal)

1. **Clonar el repositori:**
   ```bash
   git clone https://github.com/Bibinuz/Apunts-Matematiques.git
   cd Matematiques
   ```
2. **Actualitzar apunts:**
   ```bash
   git pull
   ```

---

### Pas Final: Obrir els apunts a Obsidian (per a tots els sistemes)

1. Descarrega i instal·la [Obsidian](https://obsidian.md/) (disponible per a Windows, Linux i macOS).
2. Obre Obsidian i a la pantalla inicial tria l'opció **"Obre la carpeta com a arca"** (*Open folder as vault* si tens l'aplicació en anglès).
3. Selecciona la carpeta `Matematiques` que s'ha clonat al pas anterior. L'arca d'apunts ja està a punt per llegir i navegar!

---

## Instruccions d'Ús

- **Punt d'inici:** Comença a [`Apunts/Índex.md`](Apunts/Índex.md) per veure la distribució global de totes les assignatures i els seus respectius índexs temàtics.
- **Navegació ràpida:** 
  - Prem `Ctrl + O` (o `Cmd + O` a macOS) per cercar i obrir qualsevol nota instantàniament pel seu nom.
  - Els enllaços interns tipus `[[Títol de la Nota]]` permeten navegar entre temes, lemes i referències creuades.
- **Vista de Graf (*Graph View*):** Prem `Ctrl + G` per explorar gràficament la xarxa de connexions i dependències entre conceptes matemàtics.
- **Rigor matemàtic en $\LaTeX$:** Totes les definicions, enunciats i demostracions estan tipografiats en $\LaTeX$ estàndard (`$...$` per a fórmules en línia i `$$...$$` per a blocs destacats).

---

## Ampliació i Contribucions (Forks)

Si vols fer un **fork** d'aquest repositori per afegir nous apunts, assignatures o exercicis:

1. Fes un **Fork** del projecte al teu compte de GitHub i clona'l localment.
2. Crea una branca per a les teves aportacions:
   ```bash
   git checkout -b ampliacio-apunts
   ```
3. Segueix les convencions documentades a [`GUIA_APUNTS.md`](GUIA_APUNTS.md):
   - **Notes completes:** Unitats temàtiques completes per fitxer dins de `Apunts/<Assignatura>/`.
   - **Estil i rigor:** Utilitza callouts d'Obsidian (`> [!IMPORTANT]`, `> [!NOTE]`, etc.) per a definicions, teoremes i alertes; mantén totes les demostracions pas a pas.
   - **Interconnexió:** Actualitza l'índex de l'assignatura corresponent i [`Apunts/Índex.md`](Apunts/Índex.md) amb els nous enllaços.
4. Fes `commit`, `push` i obre una **Pull Request**.

---

## Llicència

Material d'ús lliure i obert per a la comunitat d'estudiants i docents de matemàtiques.
