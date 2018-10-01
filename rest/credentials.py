#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
