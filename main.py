import os
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, "r") as f:
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=file[:-4], ln=1)
            pdf.cell(200, 10, txt=f.read(), ln=1)
pdf.output("combined.pdf")
