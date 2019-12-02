import sys
import fitz

annote_list = ["a", "b", "c", "d", "e", "f", "g"]


def Marker(doc, target_name_list):
    col = fitz.utils.getColor("white")
    changed = False
    for page in doc:
        wordlist = page.getTextWords()
        for word in wordlist:
            for target in target_name_list:
                if target in word:
                    changed = True
                    rectangle = fitz.Rect(word[:4])
                    page.drawRect(rectangle, color=col, fill=col, overlay=True)
                elif target in word[4]:
                    for annote in annote_list:
                        if target+annote in word[4]:
                            changed = True
                            rectangle = fitz.Rect(word[:4])
                            page.drawRect(rectangle, color=col,
                                          fill=col, overlay=True)
                        elif annote+target in word[4]:
                            changed = True
                            rectangle = fitz.Rect(word[:4])
                            page.drawRect(rectangle, color=col,
                                          fill=col, overlay=True)
    return [changed, doc]


def Replace(doc, target_name_list):
    black = fitz.utils.getColor("black")
    white = fitz.utils.getColor("white")
    changed = False
    for page in doc:
        wordlist = page.getTextWords()
        for word in wordlist:
            for target in target_name_list:
                if target in word:
                    changed = True
                    rectangle = fitz.Rect(word[:4])
                    page.drawRect(rectangle, color=white,
                                  fill=white, overlay=True)
                    result = -1
                    size = 8
                    print(rectangle.)
                    while(result < 0):
                        result = page.insertTextbox(
                            rectangle, "GG", expandtabs=size, fill=black, overlay=True)
                        size -= 1
                        print("["+str(size)+"]")

                        if size == 0:
                            print("This is re "+str(result)+" "+target)
                            break

                elif target in word[4]:
                    for annote in annote_list:
                        if target+annote in word[4]:
                            changed = True
                            rectangle = fitz.Rect(word[:4])
                            page.drawRect(rectangle, color=white,
                                          fill=white, overlay=True)
                            page.insertTextbox(
                                rectangle, "AAA", fill=black, overlay=True)
                        elif annote+target in word[4]:
                            changed = True
                            rectangle = fitz.Rect(word[:4])
                            page.drawRect(rectangle, color=white,
                                          fill=white, overlay=True)
                            page.insertTextbox(
                                rectangle, "buffer",  fontname="helv", expandtabs=8, fill=black, overlay=True)
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
    doc = fitz.open("./bias.pdf")
    [new_doc, doc] = Replace(doc, target_name_list)

    #####################################################
    #               Save File
    #####################################################
    if new_doc:
        doc.save("output.pdf")
    else:
        print(("Words not found, do not save new file."))


target_name_list = ["Andrew", "Tomkins",
                    "Min", "Zhang", "William", "D.", "Heavlin", "Peer", "Google"]
auto_processing(target_name_list)
