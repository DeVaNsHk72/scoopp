from pathlib import Path

from src.loader import load_repo
from src.chunker import chunk_repository
from src.embedder import get_embedding
from src.retriever import retrieve
from src.prompt import build_prompt
from src.chat import ask_llm

from src.github import is_github_url, clone_repo
from src.cache import cache_exists, load_cache, save_cache


EMBEDDING_MODEL = "mxbai-embed-large"


def main():

    repo = input("Enter repository path or GitHub URL: ").strip()

    if is_github_url(repo):
        repo = clone_repo(repo)

    repo_name = Path(repo).name

    if cache_exists(repo_name):

        print("\nLoading cached embeddings...")

        cache = load_cache(repo_name)

        chunks = cache["chunks"]
        embeddings = cache["embeddings"]

        print(f"Loaded {len(chunks)} cached chunks.")

    else:

        print("\nLoading repository...")
        files = load_repo(repo)
        print(f"Loaded {len(files)} files.")

        print("\nChunking repository...")
        chunks = chunk_repository(files)
        print(f"Created {len(chunks)} chunks.")

        print("\nGenerating embeddings (this may take a while)...")

        embeddings = []

        for i, chunk in enumerate(chunks, start=1):
            print(f"\rEmbedding {i}/{len(chunks)}", end="", flush=True)
            embeddings.append(get_embedding(chunk["chunk"]))

        print("\n")

        save_cache(
            repo_name,
            chunks,
            embeddings,
            EMBEDDING_MODEL
        )

        print("Embeddings cached successfully.")

    print("\nRepository indexed successfully!")

    while True:

        question = input("\nAsk a question (or type 'exit'): ").strip()

        if question.lower() == "exit":
            break

        retrieved_chunks = retrieve(
            question,
            chunks,
            embeddings,
            k=5
        )

        prompt = build_prompt(question, retrieved_chunks)

        answer = ask_llm(prompt)

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()