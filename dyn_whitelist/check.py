#!/usr/bin/env python3
# -*- Mode: Python; tab-width: 4; indent-tabs-mode: nil -*-
"""check_ssh_whitelist script."""

import socket

# import textwrap


def check_rules(options):
    """This is the entry function."""

    # variable did not work need to use raw string
    addrs = list(
        map(
            lambda x: x[4][0],
            socket.getaddrinfo("www.metaorg.com.", 22, type=socket.SOCK_STREAM),
        )
    )
    print(addrs)
    print("Checkem Danno!")
    return 0
