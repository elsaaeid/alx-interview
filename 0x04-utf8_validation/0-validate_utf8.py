#!/usr/bin/python3
"""
validUTF8 function
"""


def validUTF8(data):
    """
    Returns True if data
    is a valid UTF-8 encoding,
    else return False
    """
    expected_length = 0

    for num in data:
        binary_num = bin(num)[2:].zfill(8)

        if expected_length == 0:
            if binary_num.startswith("0"):
                continue
            elif binary_num.startswith("110"):
                expected_length = 2
            elif binary_num.startswith("1110"):
                expected_length = 3
            elif binary_num.startswith("11110"):
                expected_length = 4
            else:
                return False
        else:
            if not binary_num.startswith("10"):
                return False
            expected_length -= 1

    return expected_length == 0
