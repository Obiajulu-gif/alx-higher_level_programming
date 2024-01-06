
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a: an integer or float
    - b(default=98): an integer or float.

    Raises:
    -  TypeError: If a or b is not an integer or float

    Returns:
    - an integer: the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
