#!/usr/bin/python3
"""script that takes ur Github credentials
(username and password)
and uses the Github API to display your id"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=authentication)
    print(response.json().get('id'))
