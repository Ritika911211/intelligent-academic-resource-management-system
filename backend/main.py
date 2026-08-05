from services.pdf_service import extract_text_from_pdf

from fastapi import FastAPI, UploadFile, File
import os
from services.cloudinary_service import upload_pdf

app = FastAPI(title="College PYQ API")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.post("/upload-pdf")
async def upload_pdf_api(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    pdf_url = upload_pdf(file_path)
    extracted_text = extract_text_from_pdf(file_path)
   

    return {
        "message": "PDF Uploaded Successfully",
        "pdf_url": pdf_url,
        "extracted_text": extracted_text

    }
