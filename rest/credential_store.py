#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.config import Config
import keyring
import os


class CredentialStore:

    def __init__(self):
        self.id_client_prefix = "cid"
        self.secret_client_prefix = "csec"
        self.secret_user_prefix = "usec"
        self.config = Config()
        self.key_cache_location = os.curdir + self.config.GUI_DEFAULTS_FILE_LOC_PREFIX + "known-keys.txt"

    def set_client_keys(self, domain, uname, client_id, client_secret):
        cid_username = "-".join([self.id_client_prefix, uname, domain])
        csecret_username = "-".join([self.secret_client_prefix, uname, domain])
        keyring.set_password(self.config.APP_NAME, cid_username, client_id)
        keyring.set_password(self.config.APP_NAME, csecret_username, client_secret)
        with open(self.key_cache_location, "a") as cache_file:
            cache_file.write("\n".join([cid_username, csecret_username]))
            cache_file.write("\n")

    def get_client_keys(self, domain, uname):
        cid_username = "-".join([self.id_client_prefix, uname, domain])
        csecret_username = "-".join([self.secret_client_prefix, uname, domain])
        return keyring.get_password(self.config.APP_NAME, cid_username), \
               keyring.get_password(self.config.APP_NAME, csecret_username)

    def delete_client_keys(self, domain, uname):
        cid_username = "-".join([self.id_client_prefix, uname, domain])
        csecret_username = "-".join([self.secret_client_prefix, uname, domain])
        keyring.delete_password(self.config.APP_NAME, cid_username)
        keyring.delete_password(self.config.APP_NAME, csecret_username)
        new_cache = []
        with open(self.key_cache_location, "r") as cache_file:
            for line in cache_file:
                if line.strip() != cid_username and line.strip() != csecret_username:
                    new_cache.append(line)
        with open(self.key_cache_location, "w") as cache_file:
            cache_file.writelines(new_cache)

    def set_user_token(self, domain, uname, token):
        username = "-".join([self.secret_user_prefix, uname, domain])
        keyring.set_password(self.config.APP_NAME, username, token)

    def get_user_token(self, domain, uname):
        username = "-".join([self.secret_user_prefix, uname, domain])
        return keyring.get_password(self.config.APP_NAME, username)

    def delete_user_token(self, domain, uname):
        username = "-".join([self.secret_user_prefix, uname, domain])
        keyring.delete_password(self.config.APP_NAME, username)

    def existing_users_and_domains(self):
        client_ids = list()
        client_secrets = list()
        output = None
        with open(self.key_cache_location, "r") as cache_file:
            for line in cache_file:
                if line.startswith(self.id_client_prefix):
                    client_ids.append(line)
                if line.startswith(self.secret_client_prefix):
                    client_secrets.append(line)

        for cid in client_ids:
            cid_parts = cid.strip().split("-")
            username, domain = cid_parts[1], cid_parts[2]
            for csecret in client_secrets:
                csecret_parts = csecret.strip().split("-")
                if (username, domain) == (csecret_parts[1], csecret_parts[2]):
                    if output is None:
                        output = dict()
                    if domain in output.keys():
                        existing = output[domain]
                        output[domain] = existing.append(username)
                    else:
                        output[domain] = list()
                        output[domain].append(username)

        return output
