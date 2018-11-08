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

    def get_full_handle(self):
        return self.user['acct']

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
        return h.handle(self.toot['content'])

    def has_media(self):
        return any(self.toot['media_attachments'])

    def get_media(self):
        return self.toot['media_attachments']

    def is_media_sensitive(self):
        if self.toot['sensitive'] is not None:
            return self.toot['sensitive']
        return False

    def has_emoji(self):
        return self.toot['emojis'] is not None

    def get_emoji(self):
        return self.toot['emojis']

    def has_cw(self):
        return self.toot['spoiler_text'] is not None

    def get_cw(self):
        return self.toot['spoiler_text']

    def get_timestamp(self):
        return self.toot['created_at']
