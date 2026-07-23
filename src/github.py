import subprocess
from pathlib import Path

REPOS_DIR = Path("repos")
REPOS_DIR.mkdir(exist_ok=True)


def is_github_url(path):
    return path.startswith("https://github.com/")


def get_repo_name(url):
    return url.rstrip("/").split("/")[-1].replace(".git", "")


def clone_repo(url):
    repo_name = get_repo_name(url)
    repo_path = REPOS_DIR / repo_name

    if repo_path.exists():
        print(f"Using existing repository: {repo_path}")
        return str(repo_path)

    print("Cloning repository...")

    subprocess.run(
        ["git", "clone", url, str(repo_path)],
        check=True
    )

    print("Repository cloned successfully.")

    return str(repo_path)