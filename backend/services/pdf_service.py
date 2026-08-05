import pdfplumber

def extract_text_from_pdf(file_path):
    full_text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text.strip()

import fitz
import os


def convert_pdf_to_images(pdf_path, output_folder="uploads/pdf_images"):
    os.makedirs(output_folder, exist_ok=True)

    pdf_document = fitz.open(pdf_path)
    image_paths = []

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        image_path = os.path.join(
            output_folder,
            f"page_{page_number + 1}.png"
        )

        pix.save(image_path)
        image_paths.append(image_path)

    pdf_document.close()

    return image_paths

