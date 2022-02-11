#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import urllib.request, urllib.parse
from sys import argv


if __name__ == "__main__":
	url = argv[1]
	email = argv[2]
	value = {'email': email}

	data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
