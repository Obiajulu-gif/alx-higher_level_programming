#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        if request_id:
            print(request_id)
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.URLError as e:
    print("Error:", e.reason)
    sys.exit(1)
