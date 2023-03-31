#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script
(number or type)
You must use the with statement
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv

    url = argv[1]
    data = {}
    data['email'] = argv[2]
    data_values = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, data_values)
    with request.urlopen(req) as response:
        body_response = response.read().decode('utf-8')
        print(body_response)
