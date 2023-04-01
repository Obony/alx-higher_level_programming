#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Print name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    # Check that first_name and last_name are both strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        # If either parameter is not a string, raise a TypeError with a helpful message
        raise TypeError("first_name must be a string or last_name must be a string")

    # If last_name is provided (i.e., it's not an empty string), print out the full name
    if last_name:
        # Use string formatting to insert the first and last name into the output string
        print(f"My name is {first_name} {last_name}")
    # Otherwise, if last_name is not provided, print out only the first name
    else:
        print(f"My name is {first_name}")

