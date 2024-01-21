import requests
import string
from bs4 import BeautifulSoup
enter_input = input("search")
u_i = string.capwords(enter_input)
lists = u_i.split()
word = "_".join(lists)

url= "https://wikipedia.org/wiki/"+word
def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open._content,'html.parser')
    details = soup('table',{'class':'infobox'})
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and details is not None:
                for x,y in zip(heading,detail):
                    print("{} :: {}".format(x.text,y.text))
                    print("_____________________________")
        for i in range(1,3):
            print(soup('p')[i].text)
wikibot(url)
