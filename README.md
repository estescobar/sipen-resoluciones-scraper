# sipen-resoluciones-scrapper

--- 

# 📄 Descarga y combinación de resoluciones vigentes de la SIPEN

Este script en Python automatiza la descarga de todas las **resoluciones vigentes** publicadas por la Superintendencia de Pensiones (SIPEN) de la República Dominicana, directamente desde su sitio web oficial.

Puedes elegir entre tres modos de operación:

- 📥 **Descarga individual**: guarda cada resolución vigente como un archivo PDF separado.
- 📚 **Descarga combinada**: genera un solo PDF que une todas las resoluciones vigentes.
- 🔁 **Ambos**: realiza las dos tareas anteriores.

---

## ⚙️ Requisitos

Este script utiliza las siguientes librerías de Python:

- `requests`
- `beautifulsoup4`
- `PyPDF2`

Instálalas ejecutando:

```bash
pip install requests beautifulsoup4 PyPDF2
