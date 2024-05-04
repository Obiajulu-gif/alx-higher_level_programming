#!/usr/bin/python3
"""Error code #0"""
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
    sys.exit(1)
except urllib.error.URLError as e:
    print("Error:", e.reason)
    sys.exit(1)
