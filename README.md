# Apunts del Grau de Matemàtiques

Aquest repositori conté transcripcions assistides per intel·ligència artificial (IA) d'apunts presos a mà i explicacions a la pissarra durant les classes presencials del Grau de Matemàtiques. El contingut està redactat íntegrament en català amb el màxim rigor formal, estructurat en unitats temàtiques completes i optimitzat per a la visualització, edició i navegació interconnectada mitjançant **Obsidian** (o qualsevol visor de Markdown amb suport per a $\LaTeX$).

---

## Instal·lació

1. **Clonar el repositori:**
   ```bash
   https://github.com/Bibinuz/Apunts-Matematiques.git
   cd Matematiques
   ```

2. **Obrir a Obsidian:**
   - Descarrega i instal·la [Obsidian](https://obsidian.md/) si encara no el tens.
   - A la pantalla d'inici, selecciona l'opció per obrir una carpeta existent de l'equip (*Open folder*).
   - Tria la carpeta arrel d'aquest repositori (`Matematiques`).

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
