import requests
from bs4 import BeautifulSoup

link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())