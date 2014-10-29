#!/usr/bin/env python
from urllib import urlopen
from json import loads as jsonloads

def last_commit_message():
    """ Gets the message from the latest commit from the msoucy/freeform.py
    repo on GitHub and prints it to console. If for some reason it fails,
    the function will state that has no idea what it is doing.

    returns: a `str` representation of the URL for a Google Image Search
    for 'Carlton' as it may be useful at some point.
    """
    try:
        # Get the JSON blob for the master repo (currently under msoucy)
        a = urlopen("https://api.github.com/repos/msoucy/freeform.py/commits")

    # Read in the JSON and make it a dict-like
        jobj = jsonloads(a.read())

    # Print the tex
        print "The latest commit message is: '{0}'".format(
            *(jobj[0][u'commit'][u'message'],))
    except:
        # Something broke somewhere, and this isn't enterprise Java
        print "I have no idea what I am doing."

    # Its Dangerous to go alone! Take this!
    return "https://www.google.com/search?q=carlton&tbm=isch"

import this


def main():
    carlton = last_commit_message()
    pass

if __name__ == '__main__':
    main()
