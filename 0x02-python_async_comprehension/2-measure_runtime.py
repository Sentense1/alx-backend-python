#!/usr/bin/env python3
""" Module for measuring the runtime of an asynchronous operation. """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of running async_comprehension multiple times.

    Returns:
        float: Elapsed time in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    return elapsed_time


if __name__ == '__main__':
    async def main():
        """
        Main coroutine that measures and prints the total elapsed time.
        """
        return await(measure_runtime())

    print(asyncio.run(main()))
