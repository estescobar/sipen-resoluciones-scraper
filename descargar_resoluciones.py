import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger, PdfReader
from io import BytesIO
import os

# CONFIGURACIÓN
modo_descarga = "combinado"  # Opciones: "combinado", "individual", "ambos"
output_folder = "resoluciones_individuales"
output_combined = "resoluciones_vigentes_combinadas.pdf"

# Preparar carpeta si es necesario
if modo_descarga in ["individual", "ambos"]:
    os.makedirs(output_folder, exist_ok=True)

merged_pdf = PdfMerger()
vigentes_count = 0

base_url = "https://www.sipen.gob.do/resoluciones/resoluciones-de-la-sipen?page="

for page in range(1, 50):
    url = f"{base_url}{page}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error en la página {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table#normativa tbody tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        estatus = cols[3].text.strip().lower()
        if estatus == "vigente":
            pdf_tag = cols[4].find("a")
            if pdf_tag and "href" in pdf_tag.attrs:
                pdf_url = pdf_tag["href"]
                filename = pdf_url.split("/")[-1]

                try:
                    pdf_response = requests.get(pdf_url)
                    pdf_file = BytesIO(pdf_response.content)

                    # Validar que el PDF pueda ser leído
                    try:
                        PdfReader(pdf_file)
                        pdf_file.seek(0)

                        # Si modo incluye combinado
                        if modo_descarga in ["combinado", "ambos"]:
                            merged_pdf.append(pdf_file)

                        # Si modo incluye individuales
                        if modo_descarga in ["individual", "ambos"]:
                            with open(os.path.join(output_folder, filename), "wb") as f:
                                f.write(pdf_file.read())

                        vigentes_count += 1
                        print(f"Agregado: {filename}")

                    except Exception as parse_error:
                        print(f"PDF inválido (omitido): {pdf_url} - {parse_error}")

                except Exception as e:
                    print(f"Error al procesar {pdf_url}: {e}")

# Guardar el PDF combinado si aplica
if modo_descarga in ["combinado", "ambos"]:
    with open(output_combined, "wb") as f:
        merged_pdf.write(f)
    merged_pdf.close()
    print(f"\nArchivo combinado generado: {output_combined}")

print(f"\nProceso completado. Total resoluciones vigentes agregadas: {vigentes_count}")
