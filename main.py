from pdf2docx import Converter
import os

pdf_file = input("Enter PDF filename: ")

if os.path.exists(pdf_file):
    docx_file = os.path.splitext(pdf_file)[0] + ".docx"

    cv = Converter(pdf_file)

    try:
        cv.convert(docx_file)
        print(f"Converted successfully: {docx_file}")
    finally:
        cv.close()

else:
    print("PDF file not found.")