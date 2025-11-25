import PyPDF2
from io import BytesIO

def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf = PyPDF2.PdfReader(BytesIO(file_bytes))
    text = ""

    for page in pdf.pages:
        text += page.extract_text() + "\n"

    return text
