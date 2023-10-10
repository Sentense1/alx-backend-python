#!/usr/bin/env python3
"""  Module for measuring the runtime of wait_n function."""
import asyncio
from typing import Optional
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n function.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (float): The maximum delay in seconds for each call.

    Returns:
        int: The average execution time per call in seconds .
    """
    # Measure the start time using time.perf_counter().
    start_time = time.perf_counter()

    # Run the wait_n function 'n' times concurrently using asyncio.run().
    asyncio.run(wait_n(n, max_delay))

    # Measure the end time using time.perf_counter().
    end_time = time.perf_counter()

    # Calculate the total elapsed time in seconds.
    elapsed_time = end_time - start_time

    # Calculate the average execution time per call
    return elapsed_time / n
