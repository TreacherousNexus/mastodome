#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest.credentials import Credentials
from rest.notifications import Notifications
from rest.credential_store import CredentialStore


def get_existing_users_and_domains():
    stored_credentials = CredentialStore()
    return stored_credentials.existing_users_and_domains()


class Session:

    def __init__(self, domain, username):
        self.current_session = None
        self.domain = domain
        self.username = username

    def is_initialised(self):
        return self.current_session is not None

    def initialise_session(self, password):
        login = Credentials(self.domain, self.username)
        login.client_register()
        login.user_register(password)
        self.current_session = login.get_new_session()

    def initialise_session_forced(self, forced_token):
        login = Credentials(self.domain, self.username)
        login.client_register()
        login.user_register(forced_token=forced_token)
        self.current_session = login.get_new_session()

    def load_session(self, existing_session):
        self.current_session = existing_session

    def clear_session(self):
        if self.is_initialised():
            logout = Credentials(self.domain, self.username)
            logout.user_logout()
            self.current_session = None

    def send_toot(self, toot):
        if self.is_initialised():
            self.current_session.toot(toot)

    def get_account_username(self):
        if self.is_initialised():
            return self.current_session.account_verify_credentials().acct

    def get_session_username(self):
        return self.username

    def get_session_domain(self):
        return self.domain

    def get_home_stream(self):
        if self.is_initialised():
            return self.current_session.timeline_home()

    def get_local_stream(self):
        if self.is_initialised():
            return self.current_session.timeline_local()

    def get_public_stream(self):
        if self.is_initialised():
            return self.current_session.timeline_public()

    def get_notifications(self):
        if self.is_initialised():
            notifications = Notifications(self.current_session.notifications())
            notifications.process()
            return notifications.get_notifications()
