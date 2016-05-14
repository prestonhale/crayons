'''
Module for generic helper functions
'''


def extend(old, new):
    if new:
        old.update(new)

    return old

