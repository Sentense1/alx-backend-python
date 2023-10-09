#!/usr/bin/env python3
"""Asynchronous task creation module."""


import asyncio
from asyncio import create_task
from typing import Callable, Optional


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """
    Create an asyncio.Task that generates a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task[float]: An asyncio.Task representing the asynchronous operation.
    """
    task = create_task(wait_random(max_delay))
    return task
