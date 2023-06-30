#!/usr/bin/python3
"""
This script sends request to URL
"""


def main():
    """
    Send request to URL & display body response
    (handling HTTPError exception)
    """
    import urllib.request
    from urllib.error import HTTPError
    from sys import argv

    URL = argv[1]
    try:
        with urllib.request.urlopen(URL) as response:
            print(response.read().decode())
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    main()
