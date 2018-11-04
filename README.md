# Mastodome
A new Qt-based Mastodon client written in Python.

## Intro
Mastodome is a new desktop client for [Mastodon](https://en.wikipedia.org/wiki/Mastodon_(software)), a federated social network that takes all the best elements of Twitter and makes them better. More specifically:

* Ad-supported messages and bots don't clutter up your news feed
* There's no "engagement algorithms" showing you messages out of order and out of context deliberately to make you angry
* Moderation is more effective because there's more people doing it in the first place
* You can switch servers (or run your own) if you don't like the way the admin runs things
* It's harder to create a self-reinforcing bubble of unreality when the unfettered public stream is just a click away
* You have much more control over your own privacy, blocking and muting
* It's also possible to hide off-topic and NSFW conversations behind "content warnings" to avoid alienating your usual followers

The terminology is a little different too. You "toot" a message, "boost" other peoples' toots to your followers and "favourite" messages you like.
I'm convinced that in time, most people will see that Twitter doesn't have their best interests at heart and start to migrate across. Or at the very least, have an account on both systems.

For some great advice on how to get started and register, check out [this noobie guide](https://theoutline.com/post/2689/mastodon-makes-the-internet-feel-like-home-again) from [@srol@mellified.men](https://mellified.men/@srol).

## Getting started with Mastodome
To pull down the latest stable code, simply pull from bitbucket using the following commands:
```bash
$ git clone git@gitlab.com:bobstechsite/mastodome.git
```
You should now open the `DEVNOTES` file and install all the dependencies this package requires using your system's package manager and `pip3`. Once you've done so, navigate to the cloned directory and launch Mastodome with:
```bash
$ python3 mastodome.py
```
If you run into a `FileNotFoundError` on login, creating the `config/.cache` folder manually will fix it.

In future releases I will make the process of installing and running Mastodome much simpler. There will also be a user guide on the project wiki with pictures and diagrams.

## New in this release (0.2)
See `CHANGELOG` for list of in-development changes.

### Known Issues & Limitations
* 2FA is still not supported. The first time you register the app you will have to disable it on your account, register the app and then re-enable it. You will have to do this if you ever use "log out..." instead of just exiting Mastodome
* The GUI still only permits toots up to 280 characters in size (this can be changed in config)

## FAQs
### Is Mastodome open source and/or free software?
Yes!
* Mastodome is licensed under the GNU GPLv3
* All icon images are public domain and taken from Gnome's [Tango](https://commons.wikimedia.org/wiki/Tango_icons) iconset.
* The Mastodon logo and the mascot used on the login window are the property of the [Mastodon](https://github.com/tootsuite/mastodon) project and distributed under the [GNU AGPLv3](https://www.gnu.org/licenses/agpl.html).
* Custom artwork I created for Mastodome (i.e. the Mastodome icon and image in the About window) are the property of me (Bobby Moss) and shared under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

So, if you're someone who likes to use fully-free systems like [Trisquel](https://trisquel.info/) or [Parabola](https://www.parabola.nu/) you will be glad to hear that this application is safe for you to use.

### How can I contribute?
You can help by...
* Spreading the word about how awesome Mastodon is to people who don't use it yet
* Recommending the Mastodome client to your followers on Mastodon
* Writing blog posts about Mastodome
* Contributing a translation file to the project
* Reporting bugs via the Gitlab project or via Mastodon
* Contributing code, tests and documentation
* Doing anything else you think would be useful

### Why didn't you write this in C++/Rust/Java/insert favourite language?
There are a few reasons:
* Not every language has a well-supported library for Mastodon, and I don't have time to write my own
* This application is used by one user on one system, so milliseconds of latency won't matter
* Building machine-compiled versions for each processor architecture and operating system seems a bit of a chore

There are also beneficial side-effects of using Python:
* Most of the libraries I'm calling are just wrappers for machine-compiled components anyway
* I enjoy developing things with Python, so that should keep me enthused about working on the project in my free time
* There's a low barrier to entry for people to contribute (i.e. you don't need to setup a build toolchain, download an IDE or learn how to use version control first)
* Once Mastodome is installed even non-developers can inspect what Mastodome is doing and make modifications on their own machine if they like

Those last two points are particularly important to me because I want to make this software program as accessible as possible to everyone. This is why Mastodome already supports translations and will be as user-configurable as possible. I also chose to stick with well-established libraries/frameworks/UI paradigms because they work across the widest range of PCs (of varying age) and existing disability-assistance tools.

### Will Mastodome support cross-posting to multiple accounts?
I'm planning to support logging into multiple accounts with "fast switching" between them in 0.3. Cross-posting with a single toot will likely arrive in the release after in 0.4.

### Will Mastodome support cross-posting to Twitter and Facebook?
Not in the immediate future, for the following reasons:
* Both networks require me to have an account and register on their developer portal to use their closed APIs
* The keys provided to access those closed APIs can be revoked at any time and without warning, and I'd get the blame
* I don't want Mastodome to explicitly endorse the use of those networks due to their user-hostile behaviour and malicious use of non-free JavaScript

If you disagree then you're welcome to fork Mastodome and add that functionality. But my intention is to support them through a plugin framework instead. The main benefits of this approach are:
* Users will blame the plugin rather than the whole application if these services revoke API access
* We can let people who want to use those networks register their own API keys (they do this for Mastodon anyway, so it doesn't seem unreasonable to me)

### Does Mastodome support other federated web services?
Supporting other platforms is a long way off, but it's something I've started thinking about.

[GNU Social](https://www.gnu.org/software/social/), [Pleroma](https://pleroma.social/) & [Diaspora*](https://diasporafoundation.org/) are probably the most likely candidates as they're both federated microblogging services with REST APIs I can use for Mastodome.

### Will you support cross-posting to other decentralised networks and free software/open source services?
Eventually, yes! So long as there's an existing Python library (or I have the motivation to write the REST calls myself) there's no reason why I couldn't add this at some point.

### Will you support that other feature I just thought of?
Maybe. If there are they'll all be 0.x (with the "x" corresponding to the month I'm going to be working on it) and the following are intended to be the "major" pre-release versions. This is subject to change.

* 0.1: First proof of concept (released January 2018)
* 0.4: All the features I'd consider to be "core functionality"
* 0.6: Useful things like hashtags, lists & other things I notice are missing when I start using it full-time
* 0.9: Support for more federated services and a plugin interface
* 1.0: Stable release with additional installers for Windows and Mac
