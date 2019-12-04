from PDF import Reader
from PDF import Marker
from NLP import preprocess
import fitz

file = "test/acmtest3.pdf"
def main(file):
    blocks = Reader.blocks(file)
    ents = Reader.process_blocks(blocks)

    doc = fitz.open(file)

    text = Reader.read(file)
    text = text.replace("\n", " ")
    emails = preprocess.find_emails(text)
    multi_email = preprocess.find_multiple_emails(text)

    new_doc = Marker.Replace(doc, ents['PERSON'], "Person")
    new_doc = Marker.Replace(doc, ents['ORG'], "Org")
    new_doc = Marker.Replace(doc, emails, "email")
    new_doc = Marker.Replace(doc, multi_email, "multiple@ ")

    doc.save(file[:-4] + "_edited" + file[-4:])


main(file)

