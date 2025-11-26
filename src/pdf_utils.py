from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_preparation_pdf(title, prep_steps):
    """Generate a PDF (bytes) containing preparation steps for a recipe.

    Returns bytes of the PDF file.
    """
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    margin = 50
    y = height - margin
    c.setFont('Helvetica-Bold', 16)
    c.drawString(margin, y, f"Preparation: {title}")
    y -= 30
    c.setFont('Helvetica', 11)
    if not prep_steps:
        c.drawString(margin, y, 'No preparation steps available.')
    else:
        for i, step in enumerate(prep_steps, start=1):
            # wrap long lines
            text = f"{i}. {step}"
            lines = []
            max_chars = 90
            while len(text) > max_chars:
                # break at last space before max_chars
                idx = text.rfind(' ', 0, max_chars)
                if idx == -1:
                    idx = max_chars
                lines.append(text[:idx])
                text = text[idx+1:]
            lines.append(text)
            for ln in lines:
                if y < margin + 40:
                    c.showPage()
                    y = height - margin
                    c.setFont('Helvetica', 11)
                c.drawString(margin, y, ln)
                y -= 16
            y -= 6
    c.showPage()
    c.save()
    buf.seek(0)
    return buf.read()
