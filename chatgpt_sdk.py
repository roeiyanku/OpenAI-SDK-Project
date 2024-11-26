import requests


class ChatGPT:

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/chat/completions"

    def send_message(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",

        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
        }

        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code == 200:

            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"
