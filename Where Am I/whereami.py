# Author: Ayman Nedjmeddine  @Dr_AymanB
# GIT: http://github.com/IamAyman
# G+: +AymanNedjmeddine

'''
Prints out your your location based on your public ip
    and using the DuckDuckGO api
    (which you can read more about at https://DuckDuckGO.com/api )

NOTE that: this requires the python  requests lib to run
     instructions to install it are found
      here:  http://docs.python-requests.org/en/latest/user/install/
'''

from re import compile
from time import sleep
from requests import get, ConnectionError

try:
    res = [get("https://api.duckduckgo.com/?q=whats+my+ip&format=json").json()][0]["Answer"]
    pattern = compile("<a\shref=\".+\">")
    print pattern.sub("", res)[:-4]
except ConnectionError:
    print "Err!  Couldn't connect!\tPlease check your internet connection and try again."
except KeyboardInterrupt:
    print "\nThanks for using my script! BeSafe till next time (^_^)"
    sleep(2)

