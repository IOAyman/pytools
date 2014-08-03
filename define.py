#!/usr/bin/env python

from requests import get
import sys


def define(keyword):
    return get(
        'http://api.duckduckgo.com/?format=json&q=define+'+keyword
    ).json()["Definition"]


print define(sys.argv.pop())
