# Mastodome
A new Qt-based Mastodon client written in Python.

## Intro
Mastodome is a a new desktop client for [Mastodon](https://en.wikipedia.org/wiki/Mastodon_(software)), a federated social network that takes all the best elements of Twitter and makes them better. More specifically:
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
To pull down the latest stable code, simply pull from github using one of the following commands:
```
git clone https://github.com/Mastodome/mastodome-qt.git
git clone git@github.com:Mastodome/mastodome-qt.git
```
You should now open the `DEV_NOTES` file and install all the dependencies this package requires using your system's package manager and `pip`. 
Once you've done so, navigate to the cloned directory and launch Mastodome with:
```
python mastodome.py
```

In future releases I will make the process of installing and running Mastodome much simpler. There will also be a user guide on the project wiki with pictures and diagrams.

## New in this release (0.1)
* Supports Login and logout for one Mastodon account at a time (tokens are stored in the local keystore)
* Posts plain text toots up to 280 characters in size (you can edit this limit in `config/config.py`)
* Fetches read-only notifications that point at URLs
* Fetches read-only toots from your home, local and public streams
* Displays user avatars and display names next to toots and notifications
* Displays the plain-text contents of toots and whether they're a boost or reply
* Caches avatar images to save bandwidth and speed up load times (stored in `config/.cache`. This is cleared when you use `File` > `Logout...`)
* Refreshes both visible panels (use `Edit` > `Refresh` or the `F5` key)
* Supports the use of translation files (See `config/config.py` and `config/lang/en.json`)

See [this list of closed issues](https://github.com/Mastodome/mastodome-qt/milestone/1?closed=1) for a more detailed view of new features and bug-fixes.

## Known Issues
* Noticeable lag when you login, switch between streams or refresh the visible panels
* Errors are not surfaced in dialogs yet, they output to the console window
* You can't login to Mastodome if you have MFA enabled (it works if you login at least once *then* enable MFA)
* Mastodome doesn't automatically login to your previous session, you have to open the login window again
* However... it doesn't re-check your password if you've already logged in once (even if you log out) as it reuses the existing session key
* If you revoke application access or the current session from the web interface, you won't be able to login again until you manually delete entries for that domain in your local keystore
* None of the windows can be resized
* Toots with "content warnings" in the web interface are currently displayed in full and without warnings
* To view the contents of notifications and hyperlinks you have to copy the entry (highlight and `Ctrl+C`) and paste into an external program

See [this list of open bugs](https://github.com/Mastodome/mastodome-qt/issues?q=is%3Aopen+is%3Aissue+label%3Abug) for a comprehensive list

## FAQs

### What features are coming in the next release
Check out [the milestones](https://github.com/Mastodome/mastodome-qt/milestones) I've set for this project. While this is still subject to change (as during the course of development I will inevitably push some functionality out to later releases and pull in other functionality I can do sooner) it gives you a general idea of the order I'm implementing things in and when I expect to release them.

Please bear in mind that I (Bobby Moss) am just one human being doing this in my spare time in addition to a full-time job, freelance writing work, other side-projects and the usual "life" things. I'm not a miracle worker and can't implement every single piece of functionality at the same time!

Finally, there's [a list of ideas](https://github.com/Mastodome/mastodome-qt/issues?q=is%3Aopen+is%3Aissue+label%3Aidea) for features that might be included in future versions of Mastodome. They are often "provisionally" added to a milestone, but this is subject to change.

### Is Mastodome open source and/or free software?
Yes! 
* Mastodome is licensed under [the GNU General Public License v3 (or later)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html). You can see full details in the `LICENSE` file, and there is a copyright notice in all Python modules.
* Most icon images are public domain and taken from Gnome's [Tango](https://commons.wikimedia.org/wiki/Tango_icons) iconset.
* The Mastodon logo and the mascot used on the login window are the property of the [Mastodon](https://github.com/tootsuite/mastodon) project and distributed under the [GNU AGPLv3](https://www.gnu.org/licenses/agpl.html).
* Custom artwork I created for Mastodome (i.e. the Mastodome icon and image in the About window) are the property of me (Bobby Moss) and shared under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/), so as long as you don't claim you created them yourself and relicense your changes under the same terms you're free to do what you like with them.

So, if you're someone who likes to use fully-free systems like [Trisquel](https://trisquel.info/) or [Parabola](https://www.parabola.nu/) you will be glad to hear that this application is safe for you to use.

### How can I contribute?
You can help by...
* Spreading the word about how awesome Mastodon is to people who don't use it yet
* Recommending the Mastodome client to your followers on Mastodon
* Writing blog posts about Mastodome
* [Donating to the project](https://liberapay.com/bobstechsite/donate) on Liberapay
* Contributing a translation file to the project
* Reporting bugs you discover [on this page](https://github.com/Mastodome/mastodome-qt/issues) (check if if it's already been reported first!)
* [Posting ideas](https://github.com/Mastodome/mastodome-qt/issues?q=is%3Aopen+is%3Aissue+label%3Aidea) for improving Mastodome in general and/or its GUI
* Contributing code, tests and documentation
* Doing anything else you think would be useful

### How do I contribute code?
It's quite straightforward!
1. You create your own local fork of the project (use the "fork" button on Mastodome's [github project page](https://github.com/Mastodome/mastodome-qt))
1. Apply your changes in the "dev" branch
1. When you think your code is stable enough, [submit a pull request](https://github.com/Mastodome/mastodome-qt/pulls) to sync your dev branch with mine
1. As soon as I get time I'll take a look at your code and try it out
1. If it needs some tweaking I'll offer some feedback

If the code is good I'll merge it into the project. 
If I judge it to be "bad" then I won't, but I will always explain why I arrived at that decision so you have an opportunity to fix it. (If you don't agree with me, the project's license permits you to redistribute your forked version under a new name so long as it's also licensed under the GNU GPLv3 or later).

### How will my contributions be licensed?

You should take the time to read and understand the `LICENSE` file *before* contributing time and code to this project. In summary: Your code will be licensed under the GNU GPLv3 (or later) and you're granting me, every other contributor and anyone who distributes Mastodome or makes their own fork the perpetual right to use your work without being sued or paying royalties for it.

Please do not add your name, email address, website or mastodon account to code files you've contributed to. Instead add it to `credits.csv` where it will be immediately visible to everyone who downloads the code. I am planning to add a "credits" button on the `Help` > `About` screen in Mastodome 0.2, so this will also help me ensure I can display the relevant information to end users as well.

Finally, once that list starts to grow all license notices will be updated to say "Copyright © 2018 Bobby Moss and the Mastodome contributors" to acknowledge outside contributions.

### How do I add a translation or change the keyboard shortcuts?
Simply copy `en.json` from the `config/lang/` folder, edit the values next to the keys, rename it and the put your file back in the same folder.
To make use of your new translation change the `GUI_LANG` value in `config/config.py` to the name of the JSON file without the `.json` extension.

If you've made direct edits to `en.json` and permanently broken it, your best bet is to replace it with a fresh copy from the git repository.

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

Those last two points are particularly important to me because I want to make this software program as accessible as possible to everyone. This is why Mastosome already supports translations and will be as user-configurable as possible. I also chose to stick with well-established libraries/frameworks/UI paradigms because they work across the widest range of PCs (of varying age) and existing disability-assistance tools.

### Will Mastodome support cross-posting to multiple accounts?
Yes! See [the milestones page](https://github.com/Mastodome/mastodome-qt/milestones) for my latest view on when I expect that to happen.

### Will Mastodome support cross-posting to Twitter/Facebook/Google+?
Not in the immediate future, for the following reasons:
* All three networks require me to have an account and register on their developer portal to use their closed APIs
* The keys provided to access those closed APIs can be revoked at any time and without warning, and I'd get the blame
* I don't want Mastodome to explicitly endorse the use of those networks due to their user-hostile behaviour and malicious use of non-free JavaScript

If you disagree then you're welcome to fork Mastodome and add that functionality. But my intention is to support them through a plugin framework instead. The main benefits of this approach are:
* Users will blame the plugin rather than the whole application if these services revoke API access
* We can let people who want to use those networks register their own API keys (they do this for Mastodon anyway, so it doesn't seem unreasonable to me)

### Does Mastodome support GNU Social?
Not just yet. You can try it and see if it works, but its API differs quite a bit from that of Mastodon so I would expect most things to be horribly broken.

I am currently on the look-out for a GNU Social library I can import (or write a Python wrapper around) and start using within Mastodome. See [the milestones page](https://github.com/Mastodome/mastodome-qt/milestones) for a view on when support is likely to appear.

### Will you support cross-posting to other decentralised networks and free software/open source services?
Yes! I've already penciled in support for Diaspora\*, Ghost and Wordpress on [the milestones page](https://github.com/Mastodome/mastodome-qt/milestones).

### Will you support that other feature I just thought of?
Check out the [milestones list](https://github.com/bjm1904/mastodome-qt/milestones) for a summary of what I'm planning for versions up to 1.0.

They'll all be 0.x (with the "x" corresponding to the month I'm going to be working on it) and the following are intended to be the "major" pre-release versions. This is subject to change.

* 0.1: First proof of concept
* 0.4: All core functionality
* 0.6: Everything you can do in browser
* 0.9: Extra cool stuff like 3rd party integrations and RSS support
* 1.0: Stable release with additional installers for Windows and Mac
