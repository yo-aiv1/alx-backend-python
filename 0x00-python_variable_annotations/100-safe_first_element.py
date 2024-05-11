#!/usr/bin/env python3

"""Basics of Variable Annotations"""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    return tuple
    """
    if lst:
        return lst[0]
    else:
        return None
