#!/usr/bin/env python3

"""Basics of Variable Annotations"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return tuple
    """
    def MultFunc(x: float) -> float:
        return x * multiplier

    return MultFunc
