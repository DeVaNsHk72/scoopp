from ollama import embed

def get_embedding(text: str):
    response = embed(
        model="mxbai-embed-large",
        input=text
    )

    return response.embeddings[0]