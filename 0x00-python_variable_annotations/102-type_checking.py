#!/usr/bin/env python3
""" Module for type hint """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """  Validate the code using mypy. """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

# Use a tuple instead of a list
array = (12, 72, 91)

zoom_2x = zoom_array(array)

# Pass an integer as the factor
zoom_3x = zoom_array(array, 3)
