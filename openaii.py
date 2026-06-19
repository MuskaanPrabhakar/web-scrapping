from openai import OpenAI
client = OpenAI(
    base_url ="http://192.168.1.39:11434/v1",
    api_key="ollama"
)
response =client.responses.create(
    model="qwen2.5:3b",
    instructions="You have persona of Elon Musk",
    input="What's the future of AI?"
)
print(response.output_text)