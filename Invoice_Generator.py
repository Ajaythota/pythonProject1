from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path
# create a pdf invoice from excel file

myfiles = glob.glob("invoice/*.xlsx")
file = myfiles[0]
print(file)
f1=Path(file).stem
print(f1)
#f1 = +file.split('\\')
inv=f1.split('-')
ofile ="invoice/"+f1+".pdf"
print(ofile)
df_x = pd.read_excel(file,sheet_name="Sheet 1")
print(df_x)
pdf = FPDF(orientation="P", unit="mm", format="A4")
invoice= f"Invoice:{inv[0]}"
date=f"Date:{inv[1]}"
pdf.add_page()
pdf.set_font(family="times", style="B", size=12)
pdf.cell(w=50,h=12,txt=invoice, align="L",ln=1)
pdf.cell(w=50,h=12,txt=date, align="L",ln=1)
columns= list(df_x.columns)
columns=[item.replace('_',' ').title() for item in columns]
pdf.set_font(family="times", style="B", size=12)
pdf.cell(w=40, h=12, txt=columns[0], align="L", border=1)
pdf.cell(w=40, h=12, txt=columns[1],align="L", border=1)
pdf.cell(w=40, h=12, txt=columns[2], align="L", border=1)
pdf.cell(w=40, h=12, txt=columns[3],align="L", border=1)
pdf.cell(w=40, h=12, txt=columns[4], align="L", border=1, ln=1)
for index, row in df_x.iterrows():
    pdf.set_font(family="times", style="I", size=12)
    pdf.cell(w=40, h=12, txt=str(row["product_id"]), align="L", border=1)
    pdf.cell(w=40, h=12, txt=str(row["product_name"]), align="L",border=1)
    pdf.cell(w=40, h=12, txt=str(row["amount_purchased"]), align="L", border=1)
    pdf.cell(w=40, h=12, txt=str(row["price_per_unit"]), align="L", border=1)
    pdf.cell(w=40, h=12, txt=str(row["total_price"]), align="L", border=1,ln=1)

pdf.output(ofile)