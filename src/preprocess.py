import re
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z0-9\s!?]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def lemmatize(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

def preprocess(text):
    return lemmatize(clean_text(text))
