import requests
import tempfile
from .models import Picture

from django.core import files

# List of images to download
image_urls = [
    'https://upload.wikimedia.org/wikipedia/commons/b/b4/JPEG_example_JPG_RIP_100.jpg',
]

for image_url in image_urls:
    # Steam the image from the url
    request = requests.get(image_url, stream=True)

    # Was the request OK?
    if request.status_code != requests.codes.ok:
        # Nope, error handling, skip file etc etc etc
        continue

    # Get the filename from the url, used for saving later
    file_name = image_url.split('/')[-1]

    # Create a temporary file
    lf = tempfile.NamedTemporaryFile()

    # Read the streamed image in sections
    for block in request.iter_content(1024 * 8):

        # If no more file then stop
        if not block:
            break

        # Write image block to temporary file
        lf.write(block)

    # Create the model you want to save the image to
    image = Picture()

    # Save the temporary image to the model#
    # This saves the model so be sure that is it valid
    image.image.save(file_name, files.File(lf))