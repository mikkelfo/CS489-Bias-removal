

import fitz #pip install --upgrade pymupdf /PDF
from PIL import Image, ImageColor #pip install Pillow / Image library


class WriteFile() :

    def Marker(self, filename, target_name_list):
        doc = fitz.open(filename)
        for page in doc:
            # print(page.getText())
            for target_name in target_name_list:
                target = target_name
                text_instances = page.searchFor(target)
               # print(page.getTextPage().extractText(text_instances[0]))
                #text_instances = []
                #target = target_name+","
                #text_instances = text_instances + page.searchFor(target)

                # HIGHLIGHT
                for inst in text_instances:
                    highlight = page.drawRect(inst, color=ImageColor.getcolor(
                        "black", "L"), fill=ImageColor.getcolor("black", "L"), overlay=True)
        return doc

    """
    target_name_list = ["Andrew ", "Tomkins ",
                        "Min ", "Zhang", "William ", "D. ", "Heavlin"]
    """

    
    
