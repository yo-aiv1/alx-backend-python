#!/usr/bin/env python3

"""Basics of Variable Annotations"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return tuple
    """
    return [(i, len(i)) for i in lst]
