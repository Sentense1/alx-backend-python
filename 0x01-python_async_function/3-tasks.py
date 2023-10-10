#!/usr/bin/env python3
"""Asynchronous task creation module."""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that generates a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task[float]: An asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
