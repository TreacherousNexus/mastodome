#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import Config
import os


class Icons:
    def __init__(self):
        config = Config()
        path = os.curdir + config.GUI_ICON_FILE_LOC_PREFIX
        self.btnHomeIcon = path + "home.svg"
        self.btnLocalIcon = path + "local.svg"
        self.btnPublicIcon = path + "public.svg"
        self.actionLoginLockedIcon = path + "login_locked.svg"
        self.actionLoginUnlockedIcon = path + "login_unlocked.svg"
        self.actionLogoutIcon = path + "logout.svg"
        self.actionExiticon = path + "exit.svg"
        self.actionPrefIcon = path + "pref.svg"
        self.actionRefreshIcon = path + "refresh.svg"
        self.actionLinkIcon = path + "link.svg"
        self.actionSubscribeIcon = path + "sub.svg"
        self.actionHelpIcon = path + "help.svg"
        self.actionAboutIcon = path + "about.svg"


class Pics:
    def __init__(self):
        config = Config()
        path = os.curdir + config.GUI_IMG_FILE_LOC_PREFIX
        self.loginLogoImg = path + "mastodon_logo.svg"
        self.loginMascotImg = path + "mastodon_mascot.png"
        self.aboutMascoutImg = path + "mastodome_art.png"
        self.appLogoImg = path + "mastodome_logo.svg"
