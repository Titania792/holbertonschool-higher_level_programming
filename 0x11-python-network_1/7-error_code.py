#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and
displays the body of the response """
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:  # if response is not ok
        # .status_code Returns a number that indicates the status
        print("Error code: {}".format(r.status_code))
    else:
        # .text returns the content of the response, in unicode
        print(r.text)
