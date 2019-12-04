import fitz

def Replace(doc, target_name_list, type_name):
    black = fitz.utils.getColor("black")
    white = fitz.utils.getColor("white")
    for page in doc:
        for target in target_name_list:
            touch_list = page.searchFor(target)
            for touch in touch_list:
                if not abs(touch[0] - touch[2]) < 10:
                    page.drawRect(touch, color=black,
                                  fill=black, overlay=True)
                    result = -1
                    size = 8
                    while(result < 0):
                        result = page.insertTextbox(
                            touch, type_name+" "+str(target_name_list.index(target)+1), fontsize=size, expandtabs=8, fill=white, overlay=True)
                        size -= 1
                        if size == 0:
                            print("failed to replace")
                            break

