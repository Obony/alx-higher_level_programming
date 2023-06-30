#!/usr/bin/python3
"""
This script sends POST request to given URL
"""


def main():
    """
    Send POST request to URL with email parameter &
    display response body
    """
    import urllib.request
    import urllib.parse
    from sys import argv

    URL, email = argv[1], argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(URL, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())


if __name__ == '__main__':
    main()
