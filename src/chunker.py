def chunk_text(text:str, chunk_size: int =1000, overlap: int = 100):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def chunk_repository(files, chunk_size=1000, overlap=100):
    all_chunks = []

    for file in files:
        chunks = chunk_text(
            file["content"],
            chunk_size=chunk_size,
            overlap=overlap
        )

        for chunk in chunks:
            all_chunks.append({
                "path": file["path"],
                "extension": file["extension"],
                "chunk": chunk
            })

    return all_chunks