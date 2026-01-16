import requests as rq
from bs4 import BeautifulSoup
from json import dumps

URL = 'www.newsvl.ru'

site = rq.get(f"https://{URL}")

soup = BeautifulSoup(site.text, 'html.parser')

arr = []

for div in soup.find_all('div', {'class': 'story-list__item-container'}):
    head = div.find('h3')
    text = div.find('p')
    if head and text:
        arr.append([head.find('a').string, text.find('a').string])
j = dumps(arr)
f = open('data.json', 'w')
f.write(j)