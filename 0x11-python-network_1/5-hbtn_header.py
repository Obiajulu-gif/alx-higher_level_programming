#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
print(response.headers.get('X-Request-Id'))
