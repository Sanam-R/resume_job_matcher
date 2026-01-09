from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(text1: str, text2: str) -> float:
    embeddings = model.encode([text1, text2])
    return util.cos_sim(embeddings[0], embeddings[1]).item()
