#!/usr/bin/env python3
""" Module for asynchronous delay operations. """

import asyncio
from typing import Optional, List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a sorted list of random delays.

    Args:
        n (int): The number of random delays to generate.
        max_delay (float): The maximum delay in seconds.

    Returns:
        List[float]: A list of random delays sorted in ascending order.
    """
    # Create a list of tasks to execute concurrently.
    # Using list comprehension, create tasks that call the 'wait_random' coroutine
    # Each task represents an asynchronous delay operation.
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Wait for tasks to complete using asyncio.as_completed(),
    #   which returns tasks in the order they complete.
    my_list = [await task for task in asyncio.as_completed(tasks)]

    # Sort the list of delays in ascending order.
    sorted_list = sorted(my_list)

    # Return the sorted list.
    return sorted_list

if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
