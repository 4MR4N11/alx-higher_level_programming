#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).'''

import urllib.request as urllib
import urllib.error as error
import sys

if __name__ == "__main__":
    try:
        with urllib.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
