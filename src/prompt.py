def build_prompt(question, retrieved_chunks):
    context = ""

    for item in retrieved_chunks:
        context += f"File: {item['path']}\n"
        context += "```python\n"
        context += item["chunk"]
        context += "\n```\n"
        context += "-" * 60 + "\n"

    return f"""
You are an expert software engineer.

Answer ONLY using the repository context below.

Rules:
- Use only the provided context.
- Do not invent information.
- If the answer cannot be found, reply:
  "I could not find this information in the provided repository."
- Mention the relevant file path(s) whenever possible.
- Explain the code clearly.

Repository Context:

{context}

Question:
{question}

Answer:
"""