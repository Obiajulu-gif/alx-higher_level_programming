#!/usr/bin/python3
"""script that takes in a letter
and sends a post request"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
url = 'http://0.0.0.0:5000/search_user'
payload = {'q': letter}

response = requests.post(url, data=payload)

try:
    result = response.json()
    if result:
        print("[{}] {}".format(result.get('id'), result.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
