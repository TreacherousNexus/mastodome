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


from mastodon import Mastodon
from config import config
from rest import credential_store
from keyring.errors import PasswordDeleteError


class Credentials:

    def __init__(self, domain, uname):
        self.id_client = "cid-" + domain
        self.secret_client = "csec-" + domain
        self.secret_user = "usec-" + domain
        self.domain = domain
        self.uname = uname
        self.config = config.Config()
        self.credential_store = credential_store.CredentialStore()

    def is_client_registered(self):
        return None not in self.credential_store.get_client_keys(self.domain, self.uname)

    def client_register(self):
        if not self.is_client_registered():
            try:
                self.credential_store.delete_client_keys(self.domain, self.uname)
            except PasswordDeleteError:
                pass
            client_id, client_secret = Mastodon.create_app(self.config.APP_NAME,
                                                           api_base_url=self.domain,
                                                           scopes=['read', 'write', 'follow'],
                                                           website=self.config.APP_WEBSITE)
            self.credential_store.set_client_keys(self.domain, self.uname, client_id, client_secret)

    def client_unregister(self):
        if self.is_client_registered():
            try:
                self.credential_store.delete_client_keys(self.domain, self.uname)
            except PasswordDeleteError:
                raise Exception("Failed to delete client application credentials")

    def is_user_registered(self):
        return self.credential_store.get_user_token(self.domain, self.uname) is not None

    def user_register(self, cpassword=None, forced_token=None):
        if not self.is_client_registered():
            raise Exception("Client app has not been registered for this domain yet")

        if not self.is_user_registered():
            if forced_token is None:
                cid, csecret = self.credential_store.get_client_keys(self.domain, self.uname)
                mastodon = Mastodon(
                    client_id=cid,
                    client_secret=csecret,
                    api_base_url=self.domain
                )

                user_secret = mastodon.log_in(
                    username=self.uname,
                    password=cpassword,
                    scopes=['read', 'write', 'follow'],
                )
                self.credential_store.set_user_token(self.domain, self.uname, user_secret)
            else:
                self.credential_store.set_user_token(self.domain, self.uname, forced_token)

    def get_new_session(self):
        if not self.is_client_registered():
            raise Exception("Client app has not been registered for this domain yet")

        if not self.is_user_registered():
            raise Exception("User has not authenticated with this domain yet")

        cid, csecret = self.credential_store.get_client_keys(self.domain, self.uname)
        token = self.credential_store.get_user_token(self.domain, self.uname)
        return Mastodon(client_id=cid,
                        client_secret=csecret,
                        access_token=token,
                        api_base_url=self.domain
                        )

    def user_logout(self):
        self.credential_store.delete_user_token(self.domain, self.uname)

    def get_auth_request_url(self):
        cid, csecret = self.credential_store.get_client_keys(self.domain, self.uname)
        mastodon = Mastodon(
            client_id=cid,
            client_secret=csecret,
            api_base_url=self.domain
        )
        return mastodon.auth_request_url(cid)
