import requests
import json

OPENAI_API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
OPENAI_API_KEY = 'API_KEY_DO_NOT_MODIFY'

def fetch_chat_completion(messages):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "max_tokens": 150,
        "temperature": 0.1,
    }

    response = requests.post(
        OPENAI_API_ENDPOINT,
        headers=headers,
        data=json.dumps(data),
        timeout=30,
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching completion: " + response.text)

def main():
    messages = [
        {"role": "user", "content": "Define 'photosynthesis'"}
    ]
    try:
        completion = fetch_chat_completion(messages)
        generated_text = completion["choices"][0]["message"]["content"]
        print(f'Generated text: {generated_text}')
        print(f"Model used: {completion['model']}")
        print("Full response:", json.dumps(completion, indent=2))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
