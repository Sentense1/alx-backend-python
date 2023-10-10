#!/usr/bin/env python3
""" asynchronous generator that yields random integers with a 1-second delay.
"""

import asyncio
import random


async def async_generator() -> int:
    """
    Asynchronous generator that yields random integers with a 1-second delay.

    Yields:
        int: Random integers generated between 1 and 100.
    """
    for i in range(11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

if __name__ == '__main__':
    async def print_yielded_values():
        """
        Coroutine that collects values from async_generator and prints them.
        """
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
