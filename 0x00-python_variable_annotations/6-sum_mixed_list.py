#!/usr/bin/env python3

"""Basics of Variable Annotations"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returning the sum of a list
    """
    value: float = 0
    for i in mxd_lst:
        value += i
    return value
