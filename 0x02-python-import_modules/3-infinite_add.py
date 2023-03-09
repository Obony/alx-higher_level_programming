#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    size = 0

    if count == 1:
        print("{:d}".format(size))
    else:
        for i in range(1, count):
            size = size + int(argv[i])

        print("{:d}".format(size))
