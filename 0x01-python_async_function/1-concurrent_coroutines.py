#!/usr/bin/env python3


""" Module for asynchronous delay operations. """


import asyncio
from typing import Optional, List
from .0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a sorted list of random delays.

    Args:
        n (int): The number of random delays to generate.
        max_delay (float): The maximum delay in seconds.

    Returns:
        List[float]: A list of random delays sorted in ascending order.
    """
    list_delay = [wait_random(max_delay) for times in range(n)]
    sorted_list = sorted(list_delay)
    return sorted_list


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
