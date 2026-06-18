import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.w3schools.com/')
# soup = BeautifulSoup(res.text, 'html.parser') 
soup = BeautifulSoup(res.text, 'html5lib') 
# text = ''.join(soup.body) 
# print(soup.html, 'soup.body')
html = str(soup.html)
with open('html.txt', 'w', encoding='utf-8') as file:
    file.write(html)
