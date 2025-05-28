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
```

---

## 🚀 Cómo usarlo

1. Descarga o clona este repositorio.
    
2. Abre el archivo `resoluciones_sipen.py`.
    
3. En la sección de configuración inicial, elige el modo de descarga deseado:
    

```python
modo_descarga = "combinado"  # Opciones: "combinado", "individual", "ambos"
```

4. Ejecuta el script:
    

```bash
python resoluciones_sipen.py
```

5. Los resultados se guardarán según el modo seleccionado:
    

|Modo|Resultado|
|---|---|
|`individual`|Carpeta `resoluciones_individuales/` con PDFs separados|
|`combinado`|Archivo `resoluciones_vigentes_combinadas.pdf`|
|`ambos`|Ambos anteriores|

---

## 🧠 ¿Para qué puede servir?

- Consultas rápidas de normativas vigentes sin visitar múltiples páginas.
    
- Archivo de referencia para investigadores, profesionales del sector financiero o legal.
    
- Integración en flujos de trabajo automatizados de análisis normativo.

- Cargar las resoluciones a IA. 
    

---

## 📌 Notas

- El script recorre hasta 50 páginas del portal de la SIPEN. Puedes modificarlo si cambia la estructura del sitio.
    
- Si alguna resolución no es un PDF válido, el script la omitirá y continuará con las demás.
    
- Este proyecto es solo para fines educativos y de acceso público a la información.
    

---

## 📬 Contribuciones y contacto

¿Ideas para mejorar? ¿Algún problema técnico?

Puedes abrir un issue o escribirme por LinkedIn: [estescobar](https://www.linkedin.com/in/estescobar/)

---

## 🔖 Fuente de los datos

Superintendencia de Pensiones (SIPEN):
[https://www.sipen.gob.do/resoluciones/resoluciones-de-la-sipen](https://www.sipen.gob.do/resoluciones/resoluciones-de-la-sipen)

