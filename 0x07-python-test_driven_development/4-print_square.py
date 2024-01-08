#!/usr/bin/python3


def print_square(size):
    """
    Prints a square with the character '#'.

    :param size: The size length of the square (integer).
    :raises TypeError: If size is not an integer.
    :raises ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
