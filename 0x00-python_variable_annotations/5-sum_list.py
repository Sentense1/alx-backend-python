#!/usr/bin/env python3
# Takes a list input_list of floats and returns their sum as a float.
""" Takes a list of floats, and returns thier sum """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Takes a list input_list of floats and returns their sum as a float. """
    return (sum(input_list))

if __name__ == '__main__':
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
