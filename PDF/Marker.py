import sys
import fitz

annote_list = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3", "4", "5"]

####################################################################################
#                     this is the marker function it only marks                    #
####################################################################################


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

####################################################################################
#              this is the Replace function, it will replace the text              #
####################################################################################


def Replace(doc, target_name_list, type_name):
    black = fitz.utils.getColor("black")
    white = fitz.utils.getColor("white")
    changed = False
    for page in doc:
        wordlist = page.getTextWords()
        # case sensitive
        # this has one draw back, it cannot detect string directly
        for word in wordlist:  # list all the word in the pdf
            for target in target_name_list:  # list all target word
                splits = target.split()     # if it is a string we need to slit it
                for piece in splits:        # list all word in string
                    if piece in word:
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

                    # this is for the case if tomkinsa and you give tomkins
                    elif piece in word[4]:
                        for annote in annote_list:
                            if piece+annote in word[4]:
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
                            # this is for some time "1google", the annote is in front
                            elif annote+piece in word[4]:
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
        # this is case insensitive
        #   if you only want to targe "Andrew Tomkins" use this
        #   but this may not use this to detect "Min"
        for target in target_name_list:
            touch_list = page.searchFor(target)
            for touch in touch_list:
                page.drawRect(touch, color=white,
                              fill=white, overlay=True)
                result = -1
                size = 8
                while(result < 0):
                    result = page.insertTextbox(
                        touch, type_name+" "+str(target_name_list.index(target)+1), fontsize=size, expandtabs=8, fill=black, overlay=True)
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
    new_doc = Replace(doc, target_name_list, "A")

    #####################################################
    #               Save File
    #####################################################
    if new_doc:
        doc.save("output.pdf")
    else:
        print(("Words not found, do not save new file."))


target_name_list = ["Andrew Tomkins",
                    "Min Zhang", "William D. Heavlin",  "Google"]
auto_processing(target_name_list)
