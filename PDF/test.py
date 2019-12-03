import sys
import fitz

col1 = fitz.utils.getColor("red")
col2 = fitz.utils.getColor("blue")

doc = fitz.open("./bias.pdf")
page = doc.loadPage(0)
wordlist = page.getTextWords()
# for word in wordlist:
#    if "review" in word:
#        rectangle = fitz.Rect(word[:4])
#        page.insertText((
#            rectangle, "1111111", fontsize=12, fontname="helv", color=col1, fill=col2, overlay=True)
#        print(("I do go indide"))
# doc.save("output.pdf")
print(doc.getPageFontList(0))
