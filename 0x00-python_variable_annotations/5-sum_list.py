#!/usr/bin/env python3

"""Basics of Variable Annotations"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returning the sum of a list
    """
    value: float = 0
    for i in input_list:
        value += i
    return value
