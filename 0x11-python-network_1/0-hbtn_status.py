#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        utf8 = html.decode('utf-8')
        print("Body response:")
        print("\t- type: " + str(type(html)))
        print("\t- content: " + str(html))
        print("\t- utf8 content: " + str(utf8))
        