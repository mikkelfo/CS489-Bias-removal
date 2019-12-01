

import fitz #pip install --upgrade pymupdf /PDF
from PIL import Image, ImageColor #pip install Pillow / Image library


class WriteFile :
    def marker(self, filename, target_name_list):
        annote_list = ["a", "b", "c", "d", "e", "f", "g"]
        changed = False
        doc = fitz.open(filename)
        for page in doc:
            wordlist = page.getTextWords()
            for word in wordlist:
                for target in target_name_list:
                    if target in word:
                        changed = True
                        rectangle = fitz.Rect(word[:4])
                        page.drawRect(rectangle, color=ImageColor.getcolor(
                            "black", "L"), fill=ImageColor.getcolor("black", "L"), overlay=True)
                    elif target in word[4]:
                        for annote in annote_list:
                            if target+annote in word[4]:
                                changed = True
                                rectangle = fitz.Rect(word[:4])
                                page.drawRect(rectangle, color=ImageColor.getcolor(
                                    "black", "L"), fill=ImageColor.getcolor("black", "L"), overlay=True)
        return [changed, doc]

    def auto_processing(self, filename, target_name_list):
        #####################################################
        #               Display
        #####################################################
        print("Searching for the following words in document")
        for target in target_name_list:
            print(target)

        #####################################################
        #               Marking
        #####################################################
        [new_doc, doc] = self.marker(filename, target_name_list)

        #####################################################
        #               Save File
        #####################################################
        if new_doc:
            doc.save("output.pdf")
        else:
            print("Words not found, do not save new file.")


