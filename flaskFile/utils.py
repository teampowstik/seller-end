import secrets
import os

from sqlalchemy import false
from flaskFile import config

def save_image(formImage):
    randonHex = secrets.token_hex(8)
    _, fileExe = os.path.splitext(formImage.filename)
    imageName = randonHex +  fileExe
    container_client = config.get_client()
    container_client.upload_blob(imageName, formImage)
    return imageName


def get_image_url(image_name):
    container_client = config.get_client()
    url = container_client.get_blob_client(blob = image_name).url
    return url

