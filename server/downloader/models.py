import os
from django.db import models
from django.core.files import File
from urllib.request import urlretrieve


class Picture(models.Model):
    base_url = models.URLField(max_length=250)
    image_url = models.URLField(max_length=250)
    image = models.ImageField(upload_to='pictures')

    def save(self, *args, **kwargs):
        if self.image_url and not self.image:
            result = urlretrieve(self.image_url)
            self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
            )
            super(Picture, self).save(*args, **kwargs)
