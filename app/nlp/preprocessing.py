import re
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9+.# ]', '', text)

    doc = nlp(text)
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and len(token) > 2
    ]
    print('tokens', tokens)
    return " ".join(tokens)
