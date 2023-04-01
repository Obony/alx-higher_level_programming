#!/usr/bin/python3
def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    # Check that the input text is a string
    if not isinstance(text, str):
        # If it's not a string, raise a TypeError
        raise TypeError("text must be a string")

    # Initialize empty list to store formatted lines of text
    lines = []

    # Initialize empty string to store current line being built
    line = ""

    # Iterate over each character in the input text
    for char in text:
        # If the character is a period, question mark, or colon, add it to the line and terminate the line
        if char == "." or char == "?" or char == ":":
            # Add the character and two newlines to the line
            line += char + "\n\n"
            # Add the completed line (with leading/trailing whitespace removed) to the list of lines
            lines.append(line.strip())
            # Reset the line variable to an empty string
            line = ""
        else:
            # If the character is not a punctuation mark, add it to the current line
            line += char

    # If there is a line that has not yet been terminated (i.e., no period, question mark, or colon at the end of the text)
    if line:
        # Add the completed line (with leading/trailing whitespace removed) to the list of lines
        lines.append(line.strip())

    # Join the list of lines into a single string with newline characters between each line
    formatted_text = "\n".join(lines)

    # Print the formatted text
    print(formatted_text)

