from fastapi import APIRouter, UploadFile, File
from app.services.pdf_reader import extract_text_from_pdf
from app.services.openai_client import analyze_policy
from app.utils.text_cleaner import clean_text

router = APIRouter(prefix="/extract", tags=["PDF Extraction"])

@router.post("/")
async def extract(file: UploadFile = File(...)):
    # Extraer texto
    extracted_text = extract_text_from_pdf(await file.read())

    # Limpiar texto
    cleaned = clean_text(extracted_text)

    # Enviar al modelo IA
    result = analyze_policy(cleaned)

    return result
