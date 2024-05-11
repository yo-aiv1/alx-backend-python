#!/usr/bin/env python3

"""Basics of Variable Annotations"""


def sum_list(input_list: list[float]) -> float:
    """
    returning the sum of a list
    """
    value = 0
    for i in input_list:
        value += i
    return value
