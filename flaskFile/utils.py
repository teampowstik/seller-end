import secrets
from PIL import Image
import os
from flask import current_app

def save_picture(formPicture):
    random_hex = secrets.token_hex(8)
    _, fileExt = os.path.splitext(formPicture.filename)
    pictureName = random_hex + fileExt
    picturePath = os.path.join(current_app.root_path, 'static\profile_pics', pictureName)
    outputSize = (256, 256)
    i = Image.open(formPicture)
    i.thumbnail(outputSize)
    i.save(picturePath)
    return pictureName