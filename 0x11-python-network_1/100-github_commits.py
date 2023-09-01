#!/usr/bin/python3
'''Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name and the second argument
will be the owner name. You must use the packages requests and sys'''
import requests
import sys


if __name__ == "__main__":
    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(sys.argv[2], sys.argv[1]))
    for commit in resp.json()[0:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
