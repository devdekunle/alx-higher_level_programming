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

    i = len(json_response) - 1

    count = 0
    while i and count < 10:
        print(f"{json_response[i].get('sha')}: {json_response[i].get('commit').get('author').get('name')}")

        i -= 1
        count += 1
