#!/usr/bin/env python3
""" Module for type hint """
from typing import Mapping, Any, TypeVar, Union


# Define a TypeVar for the return type
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns sequence of elements,
    but the specific types of elements are not known.
    """
    if key in dct:
        return dct[key]
    else:
        return default
