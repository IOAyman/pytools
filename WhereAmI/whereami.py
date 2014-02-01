#!/usr/bin/python2
# Copyright (c) 2013,  Ayman Nedjmeddine  @Dr_AymanB
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted (for educational puroses are more appreciated) provided that the
# following conditions are met:
#
#   Redistribution of source code must retain the above copyright notice as well as these terms
#
#   Any contributor can reference himself beneath the copyright notice
#
#
# Fork at: https://github.com/IamAyman/Fast-pyTools
#
#
# This script prints out your your location based on your public ip address
#     and using the DuckDuckGO api
#     (which you can read more about at https://DuckDuckGO.com/api )


from urllib import urlopen
from json import load
from re import compile
from time import sleep

try:
    # request the information via the ddg api
    res = load(urlopen('https://api.duckduckgo.com/?q=whats+my+ip&format=json'))['Answer']
    # compile the pattern for the unwanted url in results
    pattern = compile("<a\shref=\".+\">")
    print pattern.sub("", res)[:-4]
except IOError:
    print "Err!  Couldn't connect!\tPlease check your internet connection and try again."
except KeyboardInterrupt:
    print "\nThanks for using my script! BeSafe till next time (^_^)"
    sleep(1)