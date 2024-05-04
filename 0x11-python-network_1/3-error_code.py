#!/usr/bin/python3
"""Fetches a URL and displays the body of the response."""
import urllib.request
import urllib.error

if __name__ == "__main__":
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
