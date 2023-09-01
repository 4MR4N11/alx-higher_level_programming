#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter.'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        resp = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': sys.argv[1]})
    else:
        resp = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': ""})
    try:
        json = resp.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print("Not a valid JSON")
