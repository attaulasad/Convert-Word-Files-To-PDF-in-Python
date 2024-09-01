from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.pdfgen import canvas # type: ignore

def txt_to_pdf(input_txt, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 10)

    # Open the text file
    with open(input_txt, "r") as file:  # Corrected the input_txt reference here
        text = file.readlines()

    # Initialize position
    x = 72  # 1 inch margin
    y = height - 72

    # Add each line of text to the PDF
    for line in text:
        if y < 72:  # If we're getting close to the bottom of the page
            c.showPage()  # Create a new page
            c.setFont("Helvetica", 10)
            y = height - 72
        c.drawString(x, y, line.strip())
        y -= 12  # Move down by 12 points for each line

    c.save()

# Usage
txt_to_pdf("input.TXT", "outputs.pdf")
