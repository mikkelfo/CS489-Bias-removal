import en_core_web_lg

from PDF import Reader
from PDF import Marker
from NLP import preprocess
import fitz

nlp = en_core_web_lg.load()

def main(file):
    blocks = Reader.blocks(file)
    ents = Reader.process_blocks(blocks, nlp)

    doc = fitz.open(file)

    text = Reader.read(file)
    text = text.replace("\n", " ")
    emails = preprocess.find_emails(text)
    multi_email = preprocess.find_multiple_emails(text)

    Marker.Replace(doc, ents['PERSON'], "Person")
    Marker.Replace(doc, ents['ORG'], "Org")
    Marker.Replace(doc, emails, "email")
    Marker.Replace(doc, multi_email, "multiple@ ")

    doc.save(file[:-4] + "_edited" + file[-4:])


file = "test/acmtest3.pdf"
main(file)

