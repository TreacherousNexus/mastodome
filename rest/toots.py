#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import html2text
from rest import fetch


class Toots:

    def __init__(self, toots_json):
        self.raw_toots = toots_json
        self.toots_stream = collections.OrderedDict()

    def process(self):
        self.toots_stream = collections.OrderedDict()
        for item in self.raw_toots:
            timestamp = item['created_at']
            posted_by = item['account']
            self.toots_stream[timestamp] = Toot(posted_by, item)

    def get_toots(self):
        return self.toots_stream


class Toot:

    def __init__(self, user, toot):
        self.user = user
        self.toot = toot

    def get_display_name(self):
        if not self.user['display_name']:
            return self.user['username']
        return self.user['display_name']

    def is_boost(self):
        return self.toot['reblog'] is not None

    def get_boost_with_timestamp(self):
        if self.is_boost():
            boosted_toot = self.toot['reblog']
            boosted_toot_author = boosted_toot['account']
            timestamp = boosted_toot['created_at']
            return Toot(boosted_toot_author, boosted_toot), timestamp

    def is_reply(self):
        return self.toot['in_reply_to_id'] is not None or self.toot['in_reply_to_account_id'] is not None

    def get_avatar(self, static=True):
        if static:
            return fetch.get_image(self.user['avatar_static'])
        return fetch.get_image(self.user['avatar'])

    def get_content(self):
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        return h.handle(self.toot['content'])
