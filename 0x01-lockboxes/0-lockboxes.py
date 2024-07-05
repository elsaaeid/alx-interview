#!/usr/bin/python3
"""
Mehtod to check if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Prototype to determine if all the boxes can be opened
    """
    i = 1
    while i < len(boxes) - 1:
        boolCheck = False
        y = 0
        while y < len(boxes):
            boolCheck = (i in boxes[y] and i != y)
            if boolCheck:
                break
            y += 1
        if boolCheck is False:
            return boolCheck
        i += 1
    return True
