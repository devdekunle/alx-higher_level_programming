#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = f"https://api.github.com/users/{argv[1]}"
    header = {}
    header['Accept'] = 'application/vnd.github+json'
    header['X-GitHub-Api_version'] = "2022-11-28"
    header['Authorization'] = f"Bearer {argv[2]}"

    response = requests.get(url, headers=header)
    print(response.json().get('id'))
