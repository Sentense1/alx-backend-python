#!/usr/bin/env python3
"""  module for type hint """
from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Takes a list of strings and returns a list of tuples with each string and its length."""
    return [(i, len(i)) for i in lst]
