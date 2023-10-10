#!/usr/bin/env python3
""" Provides an asynchronous coroutine for generating a random delay. """
import asyncio
import random
from typing import Optional


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random delay between 0 and max_delay and returns it.

    Args:
        max_delay (float): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay in seconds .
    """
    random_delayed = random.uniform(0, max_delay)
    await asyncio.sleep(random_delayed)
    return random_delayed
