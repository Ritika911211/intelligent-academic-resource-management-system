import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_text_with_gemini(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            "Extract all text exactly as it appears in this image. Do not summarize.",types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png",
            )
            
        ],
    )

    return response.text
