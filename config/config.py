# -*- coding: utf-8 -*-


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
        self.APP_VERSION = "0.3.5"
        self.APP_WEBSITE = "https://github.com/TreacherousNexus/mastodome-legacy"
