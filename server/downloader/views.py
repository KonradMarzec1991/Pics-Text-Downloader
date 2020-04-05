from django.http import HttpResponse
from .models import Picture
import requests
from bs4 import BeautifulSoup


BASE_URL = ''


def home(request):
    response = request.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')

    for item in img_tags:
        url = item['src']


    return HttpResponse('working!')
