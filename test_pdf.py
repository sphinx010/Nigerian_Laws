import pdfplumber
import sys

pdf_path = r"C:\Users\Ayooluwa\Documents\Lex_notes\Lex_civil\Lagos-State-High-Court-Civil-Procedure-Rules-2019-.pdf"

try:
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total pages: {len(pdf.pages)}")
        for i in range(min(5, len(pdf.pages))):
            page = pdf.pages[i]
            text = page.extract_text()
            print(f"--- Page {i+1} ---")
            print(text[:200] if text else "[No text found on this page]")
except Exception as e:
    print(f"Error: {e}")
