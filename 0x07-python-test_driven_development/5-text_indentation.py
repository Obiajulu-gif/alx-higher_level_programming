#!/usr/bin/python3

#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """text_indentation prints two new lines after sysmbols.

    Args:
        text(str): Text document

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for delimiter in ".?:":
        text = (delimiter + "\n\n").join([line.strip(" ")
                                         for line in text.split(delimiter)])
    print(text, end='')