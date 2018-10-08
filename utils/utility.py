"""
public functions
"""

# !/usr/bin/env python
# coding=utf-8

def cmp(x_str, y_str):
	x = int(x_str)
	y = int(y_str)
	if x > y:
		return 1
	elif x==y:
		return 0
	else:
		return -1


def cmp_str(element1, element2):
    """
    compare number in str format correctley
    """
    try:
        return cmp(int(element1), int(element2))
    except ValueError:
        return cmp(element1, element2)
