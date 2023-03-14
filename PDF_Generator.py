from fpdf import FPDF
import pandas as pd
df=pd.read_csv("files/topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for index, row in df.iterrows():
    #pdf.add_page(df["Pages"])
    pdf.add_page()
    pdf.set_font(family="times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    for i in range(row["Pages"] -1):
        pdf.add_page()

pdf.output("files/output.pdf")




# pdf= FPDF(orientation="P", unit="mm", format="A4")
# pdf.add_page()
# pdf.set_font(family="Times",style="B",size=12)
# pdf.cell(w=0, h=12, txt="Hello", align="L", ln=1,border=1)
# pdf.cell(w=0, h=12, txt="Hi", align="L", ln=1,border=1)
# pdf.output("output.pdf")