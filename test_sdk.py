from chatgpt_sdk import ChatGPT
import creds

# Replace 'your_api_key_here' with your actual API key
chatgpt = ChatGPT(creds.api_key)  # API key here

# Send a test message
response = chatgpt.send_message("Hello! How are you?")
print(response)
