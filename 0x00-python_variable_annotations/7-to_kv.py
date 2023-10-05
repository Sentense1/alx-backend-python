#!/usr/bin/env python3
""" Module for defining and working with type hints """
from typing import Union, Tuple

def to_kv(k: str, v: int | float) -> Tuple[Union[str, float]]:
    """ Taske a str and float/int and returns a tup,le """
    my_tuple: tuple = (k, float(v * 2))
    return my_tuple
