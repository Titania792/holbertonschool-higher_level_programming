#!/usr/bin/python3
""" Script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=(user, pwd))
    print(r.json().get('id'))
