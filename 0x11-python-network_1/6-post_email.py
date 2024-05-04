#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email"""
import requests
import sys

if len(sys.argv) < 3:
    print("Usage: {} URL email".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data)

print("Your email is: {}".format(email))
print(response.text)
