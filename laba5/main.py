import string
import requests as rq
from time import sleep
from random import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

allowed = string.ascii_letters + string.digits + " ,.?\'\"!@$%^&*()_-+=:;/абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

I = 0


def fetch(r, n):
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    global I
    I += 0.32+random()*0.32
    sleep(I)
    print(f'request: {n+1}')
    s = r.get(url=f"https://www.newsvl.ru?page={n+1}", headers=HEADERS, timeout=8)
    I = 0
    return n, s


f = open('data1.json', 'w')
f.write('{\n')
arr = []
fl = 0
with rq.Session() as r:
    with ThreadPoolExecutor(max_workers=25) as pool:
        futures = []
        for i in range(3000):
            futures.append(pool.submit(fetch, r, i))
        print('a')
        for fut in as_completed(futures):
            try:
                n, site = fut.result()
                if site.status_code != 200:
                    print(f'something wrong: {n+1}: {site.status_code}')
                    continue
                print(f'got page {n+1}')
                soup = BeautifulSoup(site.text, 'html.parser')

                for div in soup.find_all('div', {'class': 'story-list__item-container'}):
                    head = div.find('h3')
                    text = div.find('p')
                    if head and text:
                        head = "".join(ch if ch in allowed else " " for ch in head.find('a').string)
                        text = "".join(ch if ch in allowed else " " for ch in text.find('a').string)
                        if head not in arr:
                            f.write(f'{',' if fl == 1 else ''}\n\t"{head}": "{text}"')
                            fl = 1
                            arr.append(head)
                print(f'current amount: {len(arr)}')
            except Exception as e:
                print(type(e), e)
f.write('}')
f.close()
