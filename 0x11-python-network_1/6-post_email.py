#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print("Your email is:", email)
    print(r.text)
