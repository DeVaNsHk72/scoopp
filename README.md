# Scoopp

Scoopp is a lightweight GitHub Codebase RAG (Retrieval-Augmented Generation) system built entirely from scratch using Python and Ollama, without relying on LangChain or other RAG frameworks.

It indexes a code repository, generates embeddings for its source code, retrieves the most relevant code snippets using semantic search, and answers developer questions grounded in the repository.

---

## Features

* Repository indexing
* Recursive source code chunking
* Local embeddings using Ollama
* Semantic search with cosine similarity
* Grounded responses using retrieved code
* Fully local execution
* Modular architecture
* No LangChain
* No vector database

---

## Architecture

```text
Repository
     │
     ▼
Load Files
     │
     ▼
Chunk Source Code
     │
     ▼
Generate Embeddings
     │
     ▼
Store Embeddings
     │
     ▼
User Question
     │
     ▼
Embed Question
     │
     ▼
Semantic Retrieval
     │
     ▼
Top-K Relevant Chunks
     │
     ▼
Prompt Construction
     │
     ▼
Local LLM
     │
     ▼
Answer
```

---

## Project Structure

```text
scoopp/
│
├── app.py
├── requirements.txt
├── repos/
├── vector_db/
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── prompt.py
│   └── chat.py
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/scoopp.git
cd scoopp
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Ollama Models

Pull the embedding model:

```bash
ollama pull mxbai-embed-large
```

Pull the chat model:

```bash
ollama pull llama3.2
```

---

## Usage

Run the application:

```bash
python app.py
```

Provide the path to a GitHub repository when prompted.

Example:

```text
/Users/username/Downloads/numpy-main
```

Example questions:

* How does broadcasting work?
* Where is `ndarray` implemented?
* Explain the repository architecture.
* How are arrays created?
* Where is matrix multiplication implemented?

---

## Pipeline

1. Load the repository.
2. Split files into overlapping chunks.
3. Generate embeddings for every chunk.
4. Embed the user's query.
5. Retrieve the most relevant chunks using cosine similarity.
6. Build a grounded prompt.
7. Generate an answer with the local LLM.

---

## Components

### loader.py

Scans a repository recursively, filters supported source files, and loads their contents.

### chunker.py

Splits files into overlapping chunks while preserving file metadata.

### embedder.py

Generates vector embeddings using Ollama.

### retriever.py

Performs semantic retrieval using cosine similarity and returns the most relevant chunks.

### prompt.py

Constructs a grounded prompt from the retrieved context.

### chat.py

Sends the prompt to the LLM and returns the generated response.

---

## Current Limitations

* Character-based chunking
* Brute-force retrieval
* Embeddings regenerated on every run
* No persistent embedding cache
* No reranking
* No conversation memory

---

## Roadmap

* Persistent embedding cache
* FAISS integration
* AST-aware chunking
* Tree-sitter support
* GitHub repository cloning
* Streaming responses
* Hybrid retrieval
* Metadata filtering
* Multi-language support
* Conversation memory
* Web interface

---

## Why Scoopp?

Most RAG tutorials abstract away the retrieval pipeline behind high-level frameworks.

Scoopp implements each stage manually to demonstrate how Retrieval-Augmented Generation works internally:

* Document loading
* Chunking
* Embedding generation
* Semantic retrieval
* Prompt construction
* LLM interaction

The goal is to provide a clear, modular implementation that is easy to understand, extend, and improve.

---

## License

This project is licensed under the MIT License.
