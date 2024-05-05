#!/usr/bin/python3
"""script that takes a Github repository and a user name
and uses the Github API to display the last 10 commits"""

import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <repo> <owner>".format(sys.argv[0]))
        sys.exit(1)
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except ValueError:
        print("Not a valid JSON")
