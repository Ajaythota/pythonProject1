from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path
# create a pdf invoice from excel file

myfiles = glob.glob("invoice/*.xlsx")
file = myfiles[0]
f1=Path(file).stem
#f1 = file.split('\\')
inv=f1.split('-')
ofile ="invoice/"+inv[0]+".pdf"
print(ofile)
df_x = pd.read_excel(file,sheet_name="Sheet 1")
print(df_x)
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font(family="times", style="B", size=12)
pdf.cell(w=50,h=12,txt=str(inv[0]), align="L")
for index, row in df_x.iterrows():
    pdf.set_font(family="times", style="I", size=12)
    pdf.cell(w=30, h=12, txt=str(row["product_id"]), align="L", ln=1)
    pdf.cell(w=30, h=12, txt=str(row["product_name"]), align="L", ln=1)



pdf.output(ofile)