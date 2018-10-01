#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyring
from rest.credentials import Credentials
from config import config

domain = "domain.ext"
username = "user@domain.com"
password = "password"

journey = Credentials(domain, username)

# verify I'm not already registered and signed in
print journey.is_client_registered()
print journey.is_user_registered()

# Now check known good order
# IMPORTANT: You need to change config value for .defaults location or move this script up one level for it to work
print journey.client_register()
print journey.get_auth_request_url()
print journey.user_register(cpassword=password)

# Verify tokens have been stored as expected
config = config.Config()
print keyring.get_password(config.APP_NAME, journey.id_client)
print keyring.get_password(config.APP_NAME, journey.secret_client)
print keyring.get_password(config.APP_NAME, journey.secret_user)

# Send a test too
logged_in = journey.get_new_session()
logged_in.toot("This is a test from Mastodome")
