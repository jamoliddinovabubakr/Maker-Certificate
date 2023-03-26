from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def paint_pdf(ob, code):
    file_name = "media/pdfs/" + f'{code}.pdf'
    print(file_name)
    image = "static/images/certificate.jpg"

    pdf = canvas.Canvas(file_name)
    pdf.setTitle(f'{ob.first_name} {ob.last_name}')

    pdf.drawImage(image, 0, 10, 590, 820)

    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

    pdf.setFont('Vera', 32)
    pdf.drawCentredString(350, 650, "O‘zbekiston Respublikasi")

    # RGB - Red Green and Blue
    pdf.setFont("Vera", 24)
    pdf.drawCentredString(350, 600, "Malaka oshirish haqida")

    pdf.setFont("Vera", 24)
    pdf.drawCentredString(350, 560, "Sertifikat")

    pdf.setFont("Vera", 24)
    number = str(ob.cer_nomer)
    x = number.zfill(5)

    pdf.drawCentredString(350, 500, f"MO{x}")

    pdf.setFont("Vera", 20)
    pdf.drawCentredString(350, 450, f"{ob.first_name} {ob.last_name} {ob.middle_name}")

    pdf.setFont("Vera", 18)
    pdf.drawCentredString(350, 370, "2023-yil 12-21-yanvar python")
    image = "media/qr_codes/" + f'{code}.png'
    pdf.drawInlineImage(image, 80, 80, 50, 50)

    pdf.save()
