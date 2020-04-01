from django.db import models


class Picture(models.Model):
    url = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures')
