#!/usr/bin/env python2

from urllib2 import urlopen
from json import load
from subprocess import call


call('curl wttr.in/%s' % load(urlopen('http://ip-api.com/json'))['city'], shell=True)
