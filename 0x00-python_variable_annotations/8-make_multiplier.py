#!/usr/bin/env python3
""" Module for type hint """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function to multiply a float.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
