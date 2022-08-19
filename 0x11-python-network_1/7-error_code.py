#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and
displays the body of the response """
if __name__ == "__main__":
    import requests
    import sys
    with requests.get(sys.argv[1]) as response:  # open url and read response
        if response.status_code >= 400:  # if response is not ok
            # .status_code Returns a number that indicates the status
            print("Error code: {}".format(response.status_code))
        else:
            # .text returns the content of the response, in unicode
            print(response.text)
