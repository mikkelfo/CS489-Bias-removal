from PDF import Reader
from PDF import Marker
from NLP import preprocess
import fitz

def main(file):
    blocks = Reader.blocks(file)
    ents = Reader.process_blocks(blocks)

    doc = fitz.open(file)

    text = Reader.read(file)
    text = text.replace("\n", " ")
    emails = preprocess.find_emails(text)
    multi_email = preprocess.find_multiple_emails(text)

    red = fitz.utils.getColor("red")
    yellow = fitz.utils.getColor("yellow")
    blue = fitz.utils.getColor("blue")
    green = fitz.utils.getColor("green")
    cyan = fitz.utils.getColor("cyan")

    if 'PERSON' in ents:
        Marker.Replace(doc, ents['PERSON'], "Person",red)
    if 'ORG' in ents:
        Marker.Replace(doc, ents['ORG'], "Org",yellow)
    if 'GPE' in ents:
        Marker.Replace(doc, ents['GPE'], "Location",blue)
    if emails:
        Marker.Replace(doc, emails, "email",green)
    if multi_email:
        Marker.Replace(doc, multi_email, "multiple@ ",cyan)

    doc.save("output.pdf")
    #doc.save(file[:-4] + "_edited" + file[-4:])


file = "test/mikk3.pdf"
main(file)

