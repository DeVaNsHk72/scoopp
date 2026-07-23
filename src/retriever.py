import numpy as np
from src.embedder import get_embedding


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)


def retrieve(query, chunks, embeddings, k=5):
    query_embedding = get_embedding(query)

    scores = []

    for chunk, embedding in zip(chunks, embeddings):
        score = cosine_similarity(query_embedding, embedding)

        scores.append({
            "score": score,
            "path": chunk["path"],
            "extension": chunk["extension"],
            "chunk": chunk["chunk"]
        })

    scores.sort(key=lambda x: x["score"], reverse=True)

    return scores[:k]