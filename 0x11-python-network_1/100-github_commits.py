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
    header['X-GitHub-Api-Version'] = '2022-11-28'

    response = requests.get(url, headers=header)
    json_response = response.json()

    # json_response contains a list of dictionairies of the variables
    i = 0
    while i < 10:
        print(f"{json_response[i]['sha']}:\
        {json_response[i]['commit']['author']['name']}")
        i += 1
