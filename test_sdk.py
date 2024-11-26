from chatgpt_sdk import ChatGPT

# Replace 'your_api_key_here' with your actual API key
api_key = "your_api_key_here"
chatgpt = ChatGPT(api_key)

# Send a test message
response = chatgpt.send_message("Hello! How are you?")
print(response)
