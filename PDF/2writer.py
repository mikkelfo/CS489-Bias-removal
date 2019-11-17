import fitz
from PIL import Image, ImageColor


def Marker(filename, target_name_list):
    doc = fitz.open(filename)
    for page in doc:
        for target_name in target_name_list:
            target_name = " "+target_name+" "
            text_instances = page.searchFor(target_name)

            # HIGHLIGHT
            for inst in text_instances:
                highlight = page.drawRect(inst, color=ImageColor.getcolor(
                    "black", "L"), fill=ImageColor.getcolor("black", "L"), overlay=True)
    return doc


target_name_list = ["Andrew", "Tomkins",
                    "Min", "Zhang", "William", "D.", "Heavlin"]
doc = Marker("./bias.pdf", target_name_list)
doc.save("output.pdf", garbage=4, deflate=True, clean=True)
