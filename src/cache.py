import pickle
from pathlib import Path

CACHE_DIR = Path("vector_db")
CACHE_DIR.mkdir(exist_ok=True)


def get_cache_path(repo_name):
    return CACHE_DIR / f"{repo_name}.pkl"


def save_cache(repo_name, chunks, embeddings, model):
    data = {
        "chunks": chunks,
        "embeddings": embeddings,
        "model": model,
    }

    with open(get_cache_path(repo_name), "wb") as f:
        pickle.dump(data, f)


def load_cache(repo_name):
    path = get_cache_path(repo_name)

    if not path.exists():
        return None

    with open(path, "rb") as f:
        return pickle.load(f)


def cache_exists(repo_name):
    return get_cache_path(repo_name).exists()