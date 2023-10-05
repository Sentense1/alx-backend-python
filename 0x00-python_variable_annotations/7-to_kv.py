#!/usr/bin/env python3
# Taske a str and float/int and returns a tuple
""" Module for defining and working with type hints """
from typing import Union, Tuple

def to_kv(k: str, v: int | float) -> Tuple[Union[str, float]]:
    """ Taske a str and float/int and returns a tuple """
    my_tuple: tuple = (k, float(v * v))
    return my_tuple
