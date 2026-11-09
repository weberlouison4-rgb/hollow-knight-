import os

from mistralai.client import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Quelle est la capitale de la France ?",
        },
    ],
)

print(chat_response.choices[0].message.content)
