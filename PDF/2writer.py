import fitz
from PIL import Image, ImageColor

# READ IN PDF

doc = fitz.open("bias.pdf")
page = doc[0]

text = "Andrew"
text_instances = page.searchFor(text)

# HIGHLIGHT

for inst in text_instances:
    highlight = page.drawRect(inst, color=ImageColor.getcolor(
        "black", "L"), fill=ImageColor.getcolor("black", "L"), overlay=True)


# OUTPUT

doc.save("output.pdf", garbage=4, deflate=True, clean=True)
