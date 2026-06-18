##it can get block since BOT so fake useragent
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
agent = UserAgent()
res = requests.get('https://www.w3schools.com/', headers={'User-Agent': agent.chrome})
print(res.text)

