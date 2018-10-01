#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from .config import Config
import os


class Translations:

    def __init__(self):
        config = Config()
        self.translations = json.load(open(os.curdir + config.GUI_LANG_FILE_LOC_PREFIX + config.GUI_LANG + '.json'))

    def load(self, control_name):
        return self.translations[control_name]
