# import packages
import PyPDF2
import PyPDF2Highlight
import re

# open the pdf file
f = open("bias.pdf")
object = PyPDF2.PdfFileReader(f)

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "Min"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i))
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)

OUT = PyPDF2.PdfFileWriter()
OUT.addHi
