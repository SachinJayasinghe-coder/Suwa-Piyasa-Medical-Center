from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(file, app_no, name, date):
    c = canvas.Canvas(file, pagesize=A4)

    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(300, 800, "SUWA PIYASA")

    c.setFont("Helvetica", 14)
    c.drawCentredString(300, 770, "Medical Center")

    c.line(60, 750, 540, 750)

    c.setFont("Helvetica", 12)
    c.drawString(80, 710, f"Appointment Number : {app_no}")
    c.drawString(80, 680, f"Patient Name       : {name}")
    c.drawString(80, 650, f"Appointment Date   : {date}")

    c.drawString(80, 600, "Please arrive 15 minutes early.")
    c.drawString(80, 570, "Thank you for choosing Suwa Piyasa Medical Center.")

    c.save()
