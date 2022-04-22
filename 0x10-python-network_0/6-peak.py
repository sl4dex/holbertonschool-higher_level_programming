#!/usr/bin/python3
"""Find peak module"""


def find_peak(l):
    """find peak class"""
    if len(l) < 3:
        return None
    for idx in range(1, len(l) - 1):
        if l[idx] >= l[idx - 1] and l[idx] >= l[idx + 1]:
            return l[idx]
    return None
