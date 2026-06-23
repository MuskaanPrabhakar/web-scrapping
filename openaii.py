from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()
val=os.getenv('base_url')
client = OpenAI(
    base_url =val,
    api_key="ollama"
)
response =client.responses.create(
    model="qwen2.5:3b",
    instructions="You have persona of Elon Musk",
    input="What's the future of AI?"
)
print(response.output_text)