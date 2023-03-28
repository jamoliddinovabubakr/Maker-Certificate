from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def paint_pdf(ob, code):
    file_name = "media/pdfs/" + f'{code}.pdf'
    image = "static/images/certificate.jpg"

    pdf = canvas.Canvas(file_name)
    pdf.setTitle(f'{ob.first_name} {ob.last_name}')
    pdf.drawImage(image, 0, 10, 590, 820)

    pdfmetrics.registerFont(TTFont('Arimo-Italic', 'Fonts/static/Arimo-VariableFont_wght.ttf'))

    pdf.setFont('Arimo-Italic', 30)
    pdf.drawCentredString(350, 680, "O‘zbekiston Respublikasi")

    pdf.setFont("Arimo-Italic", 20)
    pdf.drawCentredString(350, 630, "Malaka oshirish haqida")

    pdf.setFont("Arimo-Italic", 30)
    pdf.drawCentredString(350, 570, "SERTIFIKAT")

    pdf.setFont("Arimo-Italic", 25)
    number = str(ob.cer_nomer)
    x = number.zfill(5)
    pdf.drawCentredString(350, 510, f"MO {x}")

    pdf.setFont("Arimo-Italic", 25)
    pdf.drawCentredString(350, 450, f"{ob.first_name} {ob.last_name}")

    pdf.setFont("Arimo-Italic", 25)
    pdf.drawCentredString(350, 425, f"{ob.middle_name}")

    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 380, "2023-yil 13-20-fevral kunlari")

    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 360, "Davlat test markazi huzuridagi Ilmiy-o'quv amaliy")
    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 340, "markazida jami 36 soatlik")

    pdf.setFont("Arimo-Italic", 15)
    course_name = str(ob.course)
    pdf.drawCentredString(350, 320, course_name)
    pdf.setFont("Arimo-Italic", 15)
    pdf.drawCentredString(350, 300, "kursi bo'yicha malakasini oshirdi")

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(210, 170, f"Boshliq: ")

    # QR code
    image = "media/qr_codes/" + f'{code}.png'
    pdf.drawInlineImage(image, 250, 150, 50, 50)

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(350, 170, f"Baratov M.K")

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(210, 120, f"Sana ")
    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(290, 120, f"22.22.2022")
    pdf.line(330, 115, 225, 115)

    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(400, 120, f"Qayd raqami ")
    pdf.setFont("Arimo-Italic", 10)
    pdf.drawCentredString(470, 120, f"23")
    pdf.line(505, 115, 440, 115)

    pdf.save()
