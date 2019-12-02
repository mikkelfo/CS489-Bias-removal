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
    return changed


def Replace(doc, target_name_list, type_name):
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
                    while(result < 0):
                        result = page.insertTextbox(
                            rectangle, type_name+" "+str(target_name_list.index(target)+1), fontsize=size, expandtabs=8, fill=black, overlay=True)
                        size -= 1
                        if size == 0:
                            print("failed to replace")
                            break

                elif target in word[4]:
                    for annote in annote_list:
                        if target+annote in word[4]:
                            changed = True
                            rectangle = fitz.Rect(word[:4])
                            page.drawRect(rectangle, color=white,
                                          fill=white, overlay=True)
                            result = -1
                            size = 8
                            while(result < 0):
                                result = page.insertTextbox(
                                    rectangle, type_name+" "+str(target_name_list.index(target)+1), fontsize=size, expandtabs=8, fill=black, overlay=True)
                                size -= 1
                                if size == 0:
                                    print("failed to replace")
                                    break
                        elif annote+target in word[4]:
                            changed = True
                            rectangle = fitz.Rect(word[:4])
                            page.drawRect(rectangle, color=white,
                                          fill=white, overlay=True)
                            result = -1
                            size = 8
                            while(result < 0):
                                result = page.insertTextbox(
                                    rectangle, type_name+" "+str(target_name_list.index(target)+1), fontsize=size, expandtabs=8, fill=black, overlay=True)
                                size -= 1
                                if size == 0:
                                    print("failed to replace")
                                    break
    return changed


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
    new_doc = Replace(doc, target_name_list, "Person")

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
