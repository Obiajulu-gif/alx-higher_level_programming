#!/usr/bin/python3

# This script takes in a URL and an email, 
# sends a POST request to the passed URL with the email as a parameter, 
# and displays the body of the response (decoded in utf-8)

import urllib.parse
import urllib.request
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)
    
url = sys.argv[1]
email = sys.argv[2]

values = {'email': email}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))
