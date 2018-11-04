#!/usr/bin/env python3
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
