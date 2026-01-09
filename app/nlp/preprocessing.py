import re
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    doc = nlp(text)
    tokens = [t.lemma_ for t in doc if not t.is_stop]
    return " ".join(tokens)
