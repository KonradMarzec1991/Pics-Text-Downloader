from django.http import HttpResponse
from .models import Picture


def home(request):
    url = "https://upload.wikimedia.org/wikipedia/commons/0/0e/Felis_silvestris_silvestris.jpg"

    pic = Picture(
        base_url='https://upload.wikimedia.org/wikipedia/',
        image_url=url
    )
    pic.save()

    return HttpResponse('working!')
