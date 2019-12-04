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

    if ents['PERSON']:
        Marker.Replace(doc, ents['PERSON'], "Person")
    if ents['ORG']:
        Marker.Replace(doc, ents['ORG'], "Org")
    if emails:
        Marker.Replace(doc, emails, "email")
    if multi_email:
        Marker.Replace(doc, multi_email, "multiple@ ")

    doc.save("output.pdf")
    #doc.save(file[:-4] + "_edited" + file[-4:])


file = "test/bias.pdf"
main(file)

