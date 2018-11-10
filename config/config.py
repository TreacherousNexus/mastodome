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



class Config:
    def __init__(self):
        self.GUI_LANG = "en"
        self.GUI_LANG_FILE_LOC_PREFIX = "/config/lang/"
        self.GUI_ICON_FILE_LOC_PREFIX = "/config/icons/"
        self.GUI_IMG_FILE_LOC_PREFIX = "/config/img/"
        self.GUI_IMG_AVATAR_CACHE_PREFIX = "/config/.cache/"
        self.GUI_DEFAULTS_FILE_LOC_PREFIX = "/config/.defaults/"
        self.GUI_TOOT_MAX_SIZE_CHARS = 280
        self.APP_NAME = "Mastodome"
        self.APP_VERSION = "0.2"
        self.APP_WEBSITE = "http://mastodome.com"
