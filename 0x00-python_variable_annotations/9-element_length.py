#!/usr/bin/env python3
# Takes an iterable of sequences and returns a list of tuples with each sequence and its length.
"""  module for type hint """
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples with each sequence and its length."""
    return [(i, len(i)) for i in lst]
