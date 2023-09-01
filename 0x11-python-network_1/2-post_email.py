#!/usr/bin/python3
'''Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)'''
import urllib.request as urllib
import urllib.parse as parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with urllib.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
