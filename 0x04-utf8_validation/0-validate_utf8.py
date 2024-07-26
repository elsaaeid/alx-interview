#!/usr/bin/python3
"""
UTF-8 validation
"""


def validUTF8(data):
    """
    Function that returns True if data
    is a valid UTF-8 encoding,
    else return False
    """
    count = 0
    index = 0

    while index < len(data):
        binary = bin(data[index]).replace('0b', '').rjust(8, '0')[-8:]
        if count == 0:
            if binary.startswith('110'):
                count = 1
            if binary.startswith('1110'):
                count = 2
            if binary.startswith('11110'):
                count = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            count -= 1

        index += 1

    if count != 0:
        return False

    return True