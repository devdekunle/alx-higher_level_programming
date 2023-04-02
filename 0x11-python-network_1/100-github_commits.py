#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
from sys import argv

if __name__ == "__main__":

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    header = {}
    header['Accept'] = 'application/vnd.github+json'

    response = requests.get(url, headers=header)
    json_response = response.json()

    # json_response contains a list of dictionairies of the variable

    i = 0
    while i < 10:
        print(json_response[i].get('sha'), end=": "
        print(json_response[i].get('commit').get('author').get('name'))

        i += 1
