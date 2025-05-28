import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger, PdfReader
from io import BytesIO

# === CONFIGURACIÓN === 
MODO_DESCARGA = "combinado"  # Opciones: "combinado", "individual", "ambos"
OUTPUT_FORLDER = "resoluciones_individuales"
OUTPUT_COMBINED = "resoluciones_vigentes_combinadas.pdf"
BASE_URL = "https://www.sipen.gob.do/resoluciones/resoluciones-de-la-sipen?page="
MAX_PAGES = 50

# === SETUP ===
if modo_descarga in {"individual", "ambos"}:
    os.makedirs(output_folder, exist_ok=True)

def fetch_html(url):
    try:
        r = requests.get(url,timeout=10)
        r.raise_for_status()
        return r.text
    except requests.RequestsException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_vigente_pdfs(html):
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table#normativa tbody tr")
    
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue
        if cols[3].text.strip().lower() != "vigente":
            continue
        link_tag = cols[4].find("a")
        if not link_tag or "href" not in link_tag.attrs:
            continue
        yield link_tag["href"]

def download_pdf(url):
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return BytesIO(r.content)
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def is_valid_pdf(file_like):
    try:
        PdfReader(file_like)
        file_like.seek(0)
        return True
    except Exception as e:
        print(f"Invalid PDF: {e}")
        return False


def save_pdf(file_like, filename):
    with open(filename, "wb") as f:
        f.write(file_like.read())

def main():
    merger = PdfMerger()
    count = 0

    for page in range(1, MAX_PAGES + 1):
        html = fetch_html(f"{BASE_URL}{page}")
        if not html:
            continue

        for pdf_url in extract_vigente_pdfs(html):
            filename = os.path.basename(pdf_url)
            pdf_file = download_pdf(pdf_url)

            if not pdf_file or not is_valid_pdf(pdf_file):
                continue

            if MODO_DESCARGA in {"combinado", "ambos"}:
                merger.append(pdf_file)
                pdf_file.seek(0)

            if MODO_DESCARGA in {"individual", "ambos"}:
                save_pdf(pdf_file, os.path.join(OUTPUT_FOLDER, filename))

            count += 1
            print(f"Agregado: {filename}")

    if MODO_DESCARGA in {"combinado", "ambos"}:
        with open(OUTPUT_COMBINED, "wb") as f:
            merger.write(f)
        merger.close()
        print(f"\nArchivo combinado generado: {OUTPUT_COMBINED}")

    print(f"\nProceso completado. Total resoluciones vigentes agregadas: {count}")

if __name__ == "__main__":
    main()
