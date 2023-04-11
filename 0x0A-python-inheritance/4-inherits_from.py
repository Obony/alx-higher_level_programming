#!/usr/bin/python3
def inherits_from(obj, a_class):
    '''
        Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False
    '''

    relatives = issubclass(obj.__class__, a_class)
    not_relatives = (obj.__class__ is not a_class)

    return (relatives and not_relatives)
