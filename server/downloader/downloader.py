import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit


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


j = 0
for url in urls:
    if not url.startswith('https') or not url.startswith('http'):
        url_parts = urlsplit(BASE_URL)
        url = f'{url_parts.scheme}://{url_parts.netloc}/{url}'
    print(url)
    image = requests.get(url)

    ext = url[url.rindex('.'):]
    filename = str(j) + ext
    save_img(image.content, filename)

    j += 1


