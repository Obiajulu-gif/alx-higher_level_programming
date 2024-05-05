#!/usr/bin/python3
"""script that takes in a letter and sends a post request"""
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

response = requests.post(url, data=data)

try:
    result = response.json()
    if result:
        print(f"[{result['id']}] {result['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
