import requests
from bs4 import BeautifulSoup

site = 'https://realpython.com/pipenv-guide/'

response = requests.get(site)
soap = BeautifulSoup(response.text, 'html.parser')

img_tags = soap.find_all('img')
urls = [img['src'] for img in img_tags]


