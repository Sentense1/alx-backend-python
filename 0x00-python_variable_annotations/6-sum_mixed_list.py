#!/usr/bin/env python3
""" TAkes a list of int and float,sums and returns a float  """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ TAkes a list of int and float,sums and returns a float """
    return sum(mxd_lst)
