#!/usr/bin/env python3
"""Module for asynchronous delay operations."""

import asyncio
import typing
from typing import List, Optional

from .3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Generate a sorted list of random delays.

    Args:
        n (int): The number of random delays to generate.
        max_delay (float): The maximum delay in seconds.

    Returns:
        List[float]: A list of random delays sorted in ascending order.
    """
    # Create a list of tasks to execute concurrently.
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for tasks to complete using asyncio.as_completed(),
    #   which returns tasks in the order they complete.
    my_list = [await task for task in asyncio.as_completed(tasks)]

    # Sort the list of delays in ascending order.
    sorted_list = sorted(my_list)

    # Return the sorted list.
    return sorted_list
