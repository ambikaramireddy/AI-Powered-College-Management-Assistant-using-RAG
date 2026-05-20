import os
from openai import OpenAI

def get_client():
    token = os.getenv("HF_TOKEN")

    return OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=token
    )

def hf_chat(prompt: str) -> str:
    client = get_client()

    model = os.getenv(
        "HF_CHAT_MODEL",
        "meta-llama/Llama-3.1-8B-Instruct"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful college assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()