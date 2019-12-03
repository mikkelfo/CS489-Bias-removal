import sys
import fitz
from PIL import Image, ImageColor

annote_list = ["a", "b", "c", "d", "e", "f", "g"]


def Marker(filename, target_name_list):
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


def auto_processing(target_name_list):
    #####################################################
    #               Display
    #####################################################
    print("Searching for the following words in document")
    for target in target_name_list:
        print(target)

    #####################################################
    #               Marking
    #####################################################
    [new_doc, doc] = Marker("./bias.pdf", target_name_list)

    #####################################################
    #               Save File
    #####################################################
    if new_doc:
        doc.save("output.pdf")
    else:
        print(("Words not found, do not save new file."))


target_name_list = ["Andrew", "Tomkins",
                    "Min", "Zhang", "William", "D.", "Heavlin"]
auto_processing(target_name_list)
