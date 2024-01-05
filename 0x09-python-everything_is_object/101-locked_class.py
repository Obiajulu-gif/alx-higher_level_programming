#!/usr/bin/python3
''' Defines a locked class '''


class LockedClass:
    '''Prevents user from dynamically creating new instance attributes,'''

    __slots__ = ['first_name']
