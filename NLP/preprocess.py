import nltk
import string
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

def normalize(text):
    text = text.lower()
    text = text.strip()
    text = remove_stopwords(text)
    text = remove_punctuation(text)

    return text

def remove_stopwords(text):
    stopwords = nltk.corpus.stopwords.words('english')
    new_string = []
    for word in text.split():
        if word not in stopwords:
            new_string.append(word)
    return ' '.join(new_string)

def remove_punctuation(text):
    for char in ["‘", "’"]:  # Weird ' from text
        text = text.replace(char, "'")
    return text.translate(str.maketrans('', '', string.punctuation))

def ents(text):
    tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))
    return [x for x in tree if type(x) == nltk.tree.Tree]

def extract_targets(entities, targets):
    # Targets could be ["PERSON", "GPE", "ORGANIZATION"]
    return [x for x in entities if x.label() in targets]
