import en_core_web_sm
import fitz     # pip install --upgrade pymupdf

def read(filename):
    doc = fitz.open(filename)
    index = 1
    text = ""
    for page in doc:
        text += "*********************** Page " + str(index) + " ***********************"
        text += '\n'
        text += page.getText("text")
        index+= 1

    return text

def blocks(filename):
    doc = fitz.open(filename)
    page = doc[0]
    x = page.getText("blocks")
    x = list(zip(*x))[4]
    string_list = [text for text in x]
    i = 1
    result = []
    while len(string_list[i].split()) < 50:
        result.append(string_list[i])
        i += 1
    return result

def process_blocks(blocks):
    nlp = en_core_web_sm.load()
    result = {}
    for lines in blocks:
        for text in lines.splitlines():
            ents = nlp(text).ents
            for ent in ents:
                if ent.label_ in result:
                    result[ent.label_] += [ent.text]
                else:
                    result[ent.label_] = [ent.text]
    return result
