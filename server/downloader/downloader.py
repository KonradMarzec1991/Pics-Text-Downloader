import os
import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://marucha.wordpress.com/2020/04/01/walczac-z-epidemia-czyli-na-progu-apokalipsy/'

DEST_DIR = 'downloads/'

response = requests.get(BASE_URL)
soap = BeautifulSoup(response.text, 'html.parser')

img_tags = soap.find_all('img')
urls = [img['src'] for img in img_tags]




