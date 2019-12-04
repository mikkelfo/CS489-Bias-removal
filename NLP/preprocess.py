import re

def normalize(text):
    text = text.lower()     # TODO: Should we do this?
    text = text.strip()

    return text

def find_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)


def find_multiple_emails(text):
    return re.findall(r'{[\w\.\, -]+}@[\w\.-]+\.\w+', text)
