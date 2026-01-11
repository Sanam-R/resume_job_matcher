from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load BERT once
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(text1: str, text2: str) -> float:
    embeddings = bert_model.encode([text1, text2])
    return util.cos_sim(embeddings[0], embeddings[1]).item()

# TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=5000
)

def tfidf_similarity(text1: str, text2: str) -> float:
    vectors = tfidf_vectorizer.fit_transform([text1, text2])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

def bert_similarity(text1: str, text2: str) -> float:
    embeddings = bert_model.encode([text1, text2])
    return util.cos_sim(embeddings[0], embeddings[1]).item()
