#!/usr/bin/env python3

"""Basics of Variable Annotations"""


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    return tuple
    """
    if key in dct:
        return dct[key]
    else:
        return default
