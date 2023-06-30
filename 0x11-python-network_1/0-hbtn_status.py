#!/usr/bin/python3
"""
This script decodes a URL
"""


def main():
    """
    Fetches URL ('https://alx-intranet.hbtn.io/status') &
    decode it
    """
    import urllib.request

    URL = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(URL) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode()))


if __name__ == '__main__':
    main()
