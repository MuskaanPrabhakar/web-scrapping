from bs4 import BeautifulSoup

# Add the encoding parameter back in!
with open('html.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    soup = BeautifulSoup(data, 'html.parser')
    
    # This will successfully print the first link it finds
    a = soup.find_all('a')
    print(a[0].attrs)