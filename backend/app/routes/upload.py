import os

from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import extract_text_from_pdf
from app.rag.vector_store import store_document
from app.services.summary_service import generate_summary

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Stores latest uploaded report text
LATEST_REPORT_TEXT = ""


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global LATEST_REPORT_TEXT

    try:

        if not file.filename.endswith(".pdf"):
            return {
                "status": "error",
                "message": "Only PDF files are allowed"
            }

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        # Save uploaded PDF
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(
            file_path
        )

        # Save latest report text
        LATEST_REPORT_TEXT = extracted_text

        # Store chunks in ChromaDB
        total_chunks = store_document(
            extracted_text
        )

        return {
            "status": "success",
            "filename": file.filename,
            "chunks_stored": total_chunks,
            "text": extracted_text
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


@router.get("/summary")
def get_summary():

    global LATEST_REPORT_TEXT

    if not LATEST_REPORT_TEXT:

        return {
            "status": "error",
            "message": "Upload a PDF first"
        }

    summary = generate_summary(
        LATEST_REPORT_TEXT
    )

    return {
        "status": "success",
        "summary": summary
    }