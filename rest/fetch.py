# -*- coding: utf-8 -*-


import shutil
import requests
import os
from config import config


def clear_image_cache():
    my_config = config.Config()
    path = os.curdir + my_config.GUI_IMG_AVATAR_CACHE_PREFIX
    for the_file in os.listdir(path):
        full_path = os.path.join(path, the_file)
        if os.path.isfile(full_path):
            os.unlink(full_path)


def get_image(url):
    my_config = config.Config()
    path = os.curdir + my_config.GUI_IMG_AVATAR_CACHE_PREFIX
    filename = url.split('/')[-1]

    if not os.path.isfile(os.path.join(path, filename)):
        response = requests.get(url, stream=True)
        with open(os.path.join(path, filename), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    return os.path.join(path, filename)
