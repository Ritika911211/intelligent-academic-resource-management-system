import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_pdf(file_path):
    result = cloudinary.uploader.upload(
        file_path,
        resource_type="raw",
        folder="college_pyq_pdfs"
    )
    return result["secure_url"]
