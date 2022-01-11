# Dynamic Whitelist

Manage firewall rules for a set of ip addresses and/or hostnames.

Reasoning...As soon as you spin up a new instance on the internet, the bad actors will
start trying break in on your ssh port. My first action is to modify the sshd_config to
make it as secure as possible and enable an alternate port for my use. I then block traffic
to port 22. I however still have the sshd_config listen on port 22 so that just in case
I make an error I can access my instance, because using firewall rules I allow my
whitelist of ip addresses to access. Some of my addresses are dynamic. My laptop goes
where I go. The address at the home where I work occasionally changes. Therefore this
tool will facilitate the management of those dynamic (and static) rules.

This is a work in progress in it's infancy. Hopefully more will come soon.

<!-- # Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ dynwhitelist --help -->
