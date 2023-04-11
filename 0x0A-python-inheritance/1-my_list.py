#!/usr/bin/python3
""" MyList Module """


class MyList(list):
    """ MyList Class """

    def ___init__(self):
        """ Initiates MyList class """
        super().__init__()

    def print_sorted(self):
        """ Prints a list in ascending order """
        print(sorted(self))
