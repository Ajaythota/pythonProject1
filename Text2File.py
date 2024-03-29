from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

#read the content from four text files and write it to 1-PDF

myfiles=glob.glob("TextPDF/*.txt")

#print(myfiles)
pdf = FPDF(orientation="P", unit="mm", format="A4")
for files in myfiles:
    fileName=Path(files).stem.capitalize()
    pdf.add_page()
    pdf.set_font(family="times", style="B", size=12)
    pdf.cell(w=50, h=12, txt=fileName, align="L")
    with open(files, "r") as file:
        #pdf.line(10,50,10,200)
        content=file.readline()
        print(content)
        pdf.set_font(family="times", style="I", size=8)
        pdf.cell(w=0, h=50, txt=content, align="R")

pdf.output("TextPDF/animal.pdf")
