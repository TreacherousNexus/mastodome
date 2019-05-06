# Mastodome
A new Qt-based Mastodon client written in Python.

## Intro
Mastodome is a new desktop client for [Mastodon](https://en.wikipedia.org/wiki/Mastodon_(software)), a federated social network that takes all the best elements of Twitter and makes them better.

**Please note**: I am currently evaluating the future direction of this project as I am running up against the limits of what I can do with PyQt, and there may be some performance problems on older systems.

This code is under an MIT license. If you want to use the Mastodome name please contact [Bobby Moss](https://github.com/TreacherousNexus).

## What is Mastodon?
Mastodon is a microblogging social network that is "federated". This means that there is no one single website that hosts Mastodon; the site is distributed across hundreds of servers, and you can even host an instance yourself.

This federated platform makes use of the [ActivityPub](https://en.wikipedia.org/wiki/ActivityPub) standard. That means Mastodon users can see content from other social networks and websites such as [Pleroma](https://pleroma.social/), [PeerTube](https://joinpeertube.org/en/) and [Pixelfed](https://pixelfed.social/) as though they have been posted on the same website.

Here are some additional advantages Mastodon has over Twitter:
* Ad-supported messages and bots do not clutter up your news feed
* There are no "engagement algorithms" that display posts out of order and out of context deliberately to make you angry
* Moderation is more effective because there are more people doing it in the first place
* You can switch servers (or run your own) if you do not like the way your administrator runs things
* It is much harder to create a self-reinforcing bubble of unreality because the unfettered public stream is just a click away
* You have much more control over your own privacy, blocking and muting
* It is also possible to hide off-topic and NSFW posts behind "content warnings" to avoid alienating your followers
* Those same "content warnings" and custom filters ensure you can avoid any online drama, politics or TV show spoilers until you want to read them
* Angry people cannot watch for posts with specific keywords or hashtags with the sole intention of finding new users to harass or troll

The terminology is also slightly different. You "toot" a message, "boost" other peoples' toots to your followers and "favourite" messages you like.
I am convinced that in time, most people will see that Twitter does not have their best interests in mind and start to migrate across. Or at the very least, have an account on both systems.

For more information about why Mastodon is a great alternative to Twitter, check out [this blog post](https://theoutline.com/post/2689/mastodon-makes-the-internet-feel-like-home-again) from [@srol@mellified.men](https://mellified.men/@srol).

For instructions on how to create a profile on Mastodon, [this blog post](https://kevq.uk/getting-started-with-mastodon/) by [@kev@fosstodon.org](https://fosstodon.org/@kev) is a great place to start.

You can follow me via [@TreacherousNexus@tech.lgbt](https://tech.lgbt/@TreacherousNexus).

## Getting started with Mastodome
To pull down the latest stable code, simply pull from gitlab using the following commands:
```bash
$ git clone https://github.com/TreacherousNexus/mastodome.git
```
You should now follow the setup steps for the application:
```bash
$ sudo apt install python3 ipython3 python3-pip gnome-keyring libgl1-mesa-glx
$ sudo pip3 install -r mastodome/requirements.txt
$ mkdir -p mastodome/config/.cache/
```

Finally, run the program itself:
```bash
$ cd mastodome
$ ./mastodome.py
```
If you want to develop Mastodome, read the `DevNotes` file for additional dependencies and supporting tools.

## New in this release (0.3.2)
See `CHANGELOG` for a full list of changes. The most notable features are:

* Simplifies setup and installs "known good" versions of pip dependencies
* Re-licenses project under MIT terms
* Removes third party assets that were licensed under AGPL

### Known Issues & Limitations
* This project is no longer in active development, so there may be bugs.
* This is still alpha stage software. You should expect to find missing functionality.
* 2FA is not supported. If you have enabled it for your account, you will need to disable it the first time you register the app, then re-enable it. You will have to do this if you ever use "log out..." instead of just exiting Mastodome
* The GUI only permits toots up to 280 characters in size by default, but this can be changed in config

## FAQs
### Is Mastodome open source and/or free software?
Yes! Mastodome is free software.
* Mastodome itself is licensed under the MIT
* All icon images are public domain and taken from Gnome's [Tango](https://commons.wikimedia.org/wiki/Tango_icons) iconset
* Custom artwork I created for Mastodome (i.e. the Mastodome icon and image in the About window) are the property of me (Bobby Moss) and shared under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

So, if you're someone who likes to use fully-free systems like [Trisquel](https://trisquel.info/) or [Parabola](https://www.parabola.nu/) you will be glad to hear that this application is safe for you to use.

### Why is development currently paused?
I am trying to create "desktop-style" functionality that mirrors the experience through the browser, but a lot of things that are easy to achieve with JavaScript are hard to achieve with PyQt. On top of that, Python is very fast when it's a wrapper for machine-compiled libraries but it becomes progressively slower the more you have to do in Python. So the more work-arounds I have to produce for PyQt and Mastodon.py (the library I use to do the REST calls) the slower performance becomes.

In principle this isn't the worst problem, however the people most likely to benefit from a desktop client are those with slow internet connections, non-standard browsers and older hardware. If this application runs badly for those people, then it defeats the purpose.

My current plan is to do a rewrite in either C++, Rust or a combination of the two. This enables me to make full use of the Qt library, write a common REST client of my own that I could use with more than one service and should run a lot better on a wide variety of hardware. This however requires a lot of planning, and a decision on whether it needs a new git repository and/or license. I will update on what I decide some time in 2019.
