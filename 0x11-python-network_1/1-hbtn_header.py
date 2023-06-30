#!/usr/bin/python3
"""
This script displays some header response values
"""


def main():
    """
    Send request to URL & display 'X-Request-Id' respone variable value
    """
    import urllib.request
    from sys import argv

    URL = argv[1]
    with urllib.request.urlopen(URL) as response:
        print(response.info().get('X-Request-Id'))


if __name__ == '__main__':
    main()
