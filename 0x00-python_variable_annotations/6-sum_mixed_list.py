#!/usr/bin/env python3
""" TAkes a list of int and float,sums and returns a float  """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ TAkes a list of int and float,sums and returns a float """
    return sum(mxd_lst)


if __name__ == '__main__':
    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
