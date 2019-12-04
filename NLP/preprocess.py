import en_core_web_lg
import re

def normalize(text):
    text = text.lower()     # TODO: Should we do this?
    text = text.strip()

    return text

def ents(text):
    nlp = en_core_web_lg.load()
    text = normalize(text)
    return nlp(text).ents

def extract(entities, target):
    return [x for x in entities if x.label_ == target]

def find_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)


def find_multiple_emails(text):
    return re.findall(r'{[\w\.\, -]+}@[\w\.-]+\.\w+', text)
