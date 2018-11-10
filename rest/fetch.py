# -*- coding: utf-8 -*-

"""

    Mastodome - Desktop Client for Mastodon
    Copyright (C) 2018 Bobby Moss bob[at]bobstechsite.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


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
