# importing required modules 
import fitz #pip install --upgrade pymupdf /PDF

class ReadFile:
    def read(self, filename):
        doc = fitz.open(filename)
        index = 1
        text = ""
        for page in doc:
            text += "*********************** Page " + str(index) + " ***********************"
            text += '\n'
            text += page.getText("text")
            index+= 1

        return text
