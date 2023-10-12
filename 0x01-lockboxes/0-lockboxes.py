#!/usr/bin/python3
"""module with canUnlockAll"""


def canUnlockAll(boxes):
    """Sees if boxes can be unlocked"""
    num_boxes = len(boxes)
    for i in range(num_boxes):
        for j in range(num_boxes):
            key = boxes[i][j]
            if (key == i):
                return True
            else:
                return False
