def is_blank(line):
    """Return True if a line is blank

    Blank lines may include whitespace, but not other characters

    :param line: String representing a line of text
    :return: Boolean that will be True if the line contains only whitespace
    """

    return None


assert is_blank("") == True
assert is_blank("\n") == True
assert is_blank("a\n") == False
assert is_blank(" \n") == True
assert is_blank("    \n") == True
assert is_blank("  b  \n") == False


def is_comment(line):
    """Return True if a line is a comment

    Comments start with `#`, but whitespace may precede that character

    :param line: String representing a line of text
    :return: Boolean that will be True if line is a comment
    """

    return None


assert is_comment("") == False
assert is_comment("\n") == False
assert is_comment(" \n") == False
assert is_comment("#\n") == True
assert is_comment("    # a\n") == True
assert is_comment("  # comment\n") == True
assert is_comment("print('#')\n") == False


# Your program begins here
# Remeber to use the functions that you tested above to help avoid errors
