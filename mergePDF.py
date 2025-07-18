from PyPDF2 import PdfWriter
import os
merger=PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)
merger.write("Merged-Pdf.pdf")
merger.close()
"""By using this program, we can merge our pdf files. We can also sort or add few more logics.
"""
