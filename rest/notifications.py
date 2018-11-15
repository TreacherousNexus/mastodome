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
from datetime import datetime, timezone, timedelta


class Notifications:

    def __init__(self, notifications_json):
        self.raw_notifications = notifications_json
        self.notifications_stream = collections.OrderedDict()

    def process(self):
        self.notifications_stream = collections.OrderedDict()
        for item in self.raw_notifications:
            timestamp = item['created_at']
            n_type = item['type']
            if n_type == "follow":
                new_notification = Notification(n_type, item['account'])
            else:
                new_notification = \
                        Notification(n_type, item['account'], item['status'])
            self.notifications_stream[timestamp] = new_notification

    def get_notifications(self):
        return self.notifications_stream


class Notification:

    def __init__(self, n_type, user, status=None):
        self.n_type = n_type
        self.user = user
        self.status = status

    def get_display_name(self):
        if not self.user['display_name']:
            return self.user['username']
        return self.user['display_name']

    def get_avatar(self, static=True):
        if static:
            return fetch.get_image(self.user['avatar_static'])
        return fetch.get_image(self.user['avatar'])

    def get_uri(self):
        return self.status['uri']

    def get_content(self):
        h = html2text.HTML2Text()
        h.ignore_links = True
        return h.handle(self.status['content'])

    def has_cw(self):
        return self.status['spoiler_text'] is not ""

    def get_cw(self):
        return self.status['spoiler_text']

    def get_full_handle(self):
        return self.user['acct']

    def has_media(self):
        return any(self.status['media_attachments'])

    def get_media(self):
        return self.status['media_attachments']

    def get_timestamp(self):
        toot_timestamp = self.status['created_at'].astimezone(timezone.utc)
        time_delta = datetime.now(timezone.utc) - toot_timestamp
        if time_delta > timedelta(days=14):
            return self.status['created_at'].strftime("%d %b '%y")
        elif time_delta > timedelta(days=1):
            return str(int(round(time_delta.total_seconds()/86400))) + "d"
        elif time_delta > timedelta(hours=1):
            return str(int(round(time_delta.total_seconds()/3600))) + "h"
        elif time_delta > timedelta(minutes=1):
            return str(int(round(time_delta.total_seconds()/60))) + "m"
        else:
            return str(int(round(time_delta.total_seconds()))) + "s"


