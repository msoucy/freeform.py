#!/usr/bin/env python
from urllib import urlopen
from json import loads as jsonloads
from pylint import epylint as lint


def last_commit_message():
    """ Gets the message from the latest commit from the msoucy/freeform.py
    repo on GitHub and prints it to console. If for some reason it fails,
    the function will state that has no idea what it is doing.

    returns: A string that represents the GitHub username of the last
    committer. If there was a problem, return None.
    """
    try:
        # Get the JSON blob for the master repo (currently under msoucy)
        a = urlopen("https://api.github.com/repos/msoucy/freeform.py/commits")

        # Read in the JSON and make it a dict-like
        jobj = jsonloads(a.read())

        # Print the message of the last commit
        print "The latest commit message is: '{0}'".format(
            *(jobj[0][u'commit'][u'message'],))
    except:
        # Something broke somewhere, and this isn't enterprise Java
        print "I have no idea what I am doing."
        jobj = None

    # return the last committer
    return jobj[0][u'author'][u'login'] if jobj else None

def lint_the_things():
    (pylint_stdout, pylint_stderr) = lint.py_run(__file__, True)
    lines = [line for line in pylint_stdout.readlines() if not line.startswith('***')]
    print("PyLint Results")
    for line in lines:
        print("\t{0}".format(line))
    return lines

import this


def main():
    last_author = last_commit_message()
    lint_result = lint_the_things()
    pass

if __name__ == '__main__':
    main()

