#!/usr/bin/env python
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

import keyring
from rest.credentials import Credentials
from config import config

domain = "domain.ext"
username = "user@domain.com"
password = "password"

journey = Credentials(domain)

# verify I'm not already registered and signed in
print journey.is_client_registered()
print journey.is_user_registered()

# Now check known good order
journey.client_register()
journey.user_register(username, password)

# Verify tokens have been stored as expected
print keyring.get_password(config.APP_NAME, journey.id_client)
print keyring.get_password(config.APP_NAME, journey.secret_client)
print keyring.get_password(config.APP_NAME, journey.secret_user)

# Send a test too
logged_in = journey.get_new_session()
logged_in.toot("This is a test from Mastodome")
