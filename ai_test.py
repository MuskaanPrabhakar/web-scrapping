# #openrouter
# import requests
# import json

# # First API call with reasoning
# response = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": "Bearer api_key",
#     "Content-Type": "application/json",
#   },
#   data=json.dumps({
#     "model": "openrouter/free",
#     "messages": [
#         {
#           "role": "user",
#           "content": "How many r's are in the word 'strawberry'?"
#         }
#       ],
#     "reasoning": {"enabled": False}
#   })
# )

# # Extract the assistant message with reasoning_details
# response = response.json()
# response = response['choices'][0]['message']

# # Preserve the assistant message with reasoning_details
# messages = [
#   {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
#   {
#     "role": "assistant",
#     "content": response.get('content'),
#     "reasoning_details": response.get('reasoning_details')  # Pass back unmodified
#   },
#   {"role": "user", "content": "Are you sure? Think carefully."}
# ]

# # Second API call - model continues reasoning from where it left off
# response2 = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   data=json.dumps({
#     "model": "openrouter/free",
#     "messages": messages,  # Includes preserved reasoning_details
#     "reasoning": {"enabled": False}
#   })
# )
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()
val= os.getenv('OPENROUTER_API_KEY')
client = OpenAI(
    base_url ="https://openrouter.ai/api/v1",
    api_key=val
)
response =client.responses.create(
    model="nex-agi/nex-n2-pro:free",
    instructions="You have persona of Elon Musk",
    input="What's the future of AI?"
)
print(response.output_text)