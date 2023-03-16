from fpdf import FPDF
import pandas as pd
df=pd.read_csv("files/topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for index, row in df.iterrows():
    #pdf.add_page(df["Pages"])
    pdf.add_page()
  #se the header
    pdf.set_font(family="times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for y in range(20, 240, 10): #lines on the page
        pdf.line(10, y, 200, y)
    #set the footer
    pdf.ln(240)
    pdf.set_font(family="times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] -1):
        pdf.add_page()
        # set the header
        pdf.set_font(family="times", style="B", size=12)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        for y in range(20, 240, 10):  #lines on the page
            pdf.line(10, y, 200, y)

        # set the footer
        pdf.ln(240)
        pdf.set_font(family="times", style="I", size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("files/output.pdf")




# pdf= FPDF(orientation="P", unit="mm", format="A4")
# pdf.add_page()
# pdf.set_font(family="Times",style="B",size=12)
# pdf.cell(w=0, h=12, txt="Hello", align="L", ln=1,border=1)
# pdf.cell(w=0, h=12, txt="Hi", align="L", ln=1,border=1)
# pdf.output("output.pdf")