#!/usr/bin/python3
"""
This script sends request to URL
"""


def main():
    """
    Send request to URL & display response body
    (handling Error codes using 'requests' pckge)
    """
    import requests
    from sys import argv

    URL = argv[1]
    res = requests.get(URL)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == '__main__':
    main()
