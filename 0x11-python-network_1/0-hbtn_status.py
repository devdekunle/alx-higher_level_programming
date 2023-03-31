#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following
example (tabulation before -)
You must use a with statement
"""

if __name__ == "__main__":

    import urllib.request as request


    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body_response = response.read()
        print("Body response:")
        print(f'\t- type: {type(body_response)}')
        print(f'\t- content: {body_response}')
        print(f'\t- uft8 content: {body_response.decode("utf-8")}')

