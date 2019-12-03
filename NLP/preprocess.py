import en_core_web_lg

def normalize(text):
    text = text.lower() # TODO: Should we do this?
    text = text.strip()

    return text

def ents(text):
    nlp = en_core_web_lg.load()
    text = normalize(text)
    return nlp(text).ents

def extract(entities, target):
    return [x for x in entities if x.label_ == target]
