#!/usr/bin/python3
"""
This script displays some header response values
(using 'requests' pckge)
"""


def main():
    """
    Send request to URL & display 'X-Request-Id' response variable value
    (using 'requests' pckge)
    """
    import requests
    from sys import argv

    URL = argv[1]
    res = requests.get(URL)
    print(res.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
