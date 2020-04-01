from django.http import HttpResponse
from .models import Picture


def home(request):
    from django.core import files
    from io import BytesIO
    import requests

    url = "https://upload.wikimedia.org/wikipedia/commons/0/0e/Felis_silvestris_silvestris.jpg"

    pic = Picture()
    pic.base_url = 'https://upload.wikimedia.org/wikipedia/'
    pic.image_url = url
    pic.get_remote_image()
    pic.save()

    return HttpResponse('working!')
