url = input("Enter the url of website you want summary of: ")

import requests
from bs4 import BeautifulSoup

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser') 
content = soup.find_all(["h1", "h2", "h3", "p"])

web_summary = "".join(
    tag.get_text(" ", strip=True)
    for tag in content
)
with open('web_summary.txt', 'w', encoding='utf-8') as file:
    file.write(web_summary)

from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()
val= os.getenv('OPENROUTER_API_KEY')
client = OpenAI(
    base_url ="https://openrouter.ai/api/v1",
    api_key=val
)
with open("web_summary.txt", "r", encoding="utf-8") as f:
    text = f.read()
response =client.responses.create(
    model="nex-agi/nex-n2-pro:free",
    instructions="You have to extract all text from file and produce full information summary in about 1/4th words",
    input=f"{text}"
)
print(response.output_text)

