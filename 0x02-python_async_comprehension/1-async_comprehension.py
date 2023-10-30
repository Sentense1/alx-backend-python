#!/usr/bin/env python3
""" Asynchronous comprehension with an async generator. """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension that collects values from async_generator.

    Returns:
        list: List of values collected asynchronously.
    """
    result = [i async for i in async_generator()]
    return result


if __name__ == '__main__':
    async def main():
        """
        Main coroutine that runs async_comprehension and prints the result.
        """
        print(await async_comprehension())

    asyncio.run(main())
