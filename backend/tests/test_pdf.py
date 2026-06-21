from app.services.pdf_service import extract_text_from_pdf

pdf_text = extract_text_from_pdf("sample_report.pdf")

print("=" * 50)
print("EXTRACTED TEXT")
print("=" * 50)

print(pdf_text)

print("=" * 50)
print("TOTAL CHARACTERS:", len(pdf_text))