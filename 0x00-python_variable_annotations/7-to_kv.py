#!/usr/bin/env python3
"""
Module for defining and working with type hints
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v, and returns a tuple.
    """
    return k, float(v * v)
