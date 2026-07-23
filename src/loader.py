from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "venv",
    ".venv",
    "node_modules",
    "build",
    "dist",
    "__pycache__"
}

TEXT_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx",
    ".java", ".cpp", ".c", ".h", ".hpp",
    ".md", ".txt", ".json", ".yaml", ".yml",
    ".toml", ".html", ".css", ".sql",
    ".go", ".rs", ".sh"
}


def load_repo(repo_path):
    repo_path = Path(repo_path)

    files = []

    for file in repo_path.rglob("*"):

        if not file.is_file():
            continue

        if any(parent.name in IGNORE_DIRS for parent in file.parents):
            continue

        if file.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        try:
            content = file.read_text(encoding="utf-8")
        except Exception:
            continue

        files.append({
            "path": str(file),
            "extension": file.suffix,
            "content": content
        })

    return files