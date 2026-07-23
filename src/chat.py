from ollama import chat


def ask_llm(prompt, model="qwen3:30b"):
    response = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content