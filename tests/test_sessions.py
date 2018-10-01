#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest import api, toots

domain = "domain.ext"
username = "user@domain.com"
password = "password"

test_session = api.Session(domain, username)
test_session.clear_session()    # Optional. You may wish to comment it out if running a lot of tests in quick succession
test_session.initialise_session(password)
test_session.send_toot("This is a test from Mastodome")

print(test_session.get_session_username())

print(test_session.get_home_stream())
print(test_session.get_local_stream())
print(test_session.get_public_stream())
print(test_session.get_notifications())

home_stream = toots.Toots(test_session.get_home_stream())
home_stream.process()

for timestamp, toot in list(home_stream.get_toots().items()):
    if toot.is_boost():
        boosted_toot, boosted_timestamp = toot.get_boost_with_timestamp()
        print(toot.get_display_name() + " boosted " + boosted_toot.get_display_name() + "'s toot.")
    elif toot.is_reply():
        print(toot.get_display_name() + " tooted in reply to someone.")
    else:
        print(toot.get_display_name() + " created a brand new toot.")
    print(toot.get_content())
    print(str(timestamp))


for item in list(test_session.get_notifications()):
    entry_type = item['type']
    entry_created_by = item['account']
    entry_created_at = item['created_at']

    display_name = entry_created_by['display_name']
    if not display_name:
        display_name = entry_created_by['username']

    if entry_type == "mention":
        toot_containing_mention = item['status']
        print(display_name + " mentioned you in " + toot_containing_mention['uri'] + " at " + str(entry_created_at))
    elif entry_type == "reblog":
        toot_boosted = item['status']
        print(display_name + " boosted " + toot_boosted['uri'] + " at " + str(entry_created_at))
    elif entry_type == "favourite":
        toot_favourited = item['status']
        print(display_name + " favourited " + toot_favourited['uri'] + " at " + str(entry_created_at))
    elif entry_type == "follow":
        print("Followed by " + display_name + " at " + str(entry_created_at))
