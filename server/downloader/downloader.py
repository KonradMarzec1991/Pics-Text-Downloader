import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from .models import Picture


BASE_URL = 'https://marucha.wordpress.com/2020/04/01/walczac-z-epidemia-czyli-na-progu-apokalipsy/'

DEST_DIR = 'downloads/'

response = requests.get(BASE_URL)
soap = BeautifulSoup(response.text, 'html.parser')

img_tags = soap.find_all('img')
urls = [img['src'] for img in img_tags]


def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename)
    print(path)
    with open(path, 'wb') as fp:
        fp.write(img)


def clean_url(url):
    if not url.startswith('http'):
        pieces = urlsplit(BASE_URL)
        print(pieces.scheme)
        start = ''

        if url.startswith('//'):
            start = pieces.scheme + ':'

        return start + url
    else:
        return url


j = 0
for url in urls:
    url = clean_url(url)
    image = requests.get(url)

    ext = url[url.rindex('.'):]
    filename = str(j) + ext

    pic = Picture(url=url, img=image.content)
    pic.save()


    j += 1


