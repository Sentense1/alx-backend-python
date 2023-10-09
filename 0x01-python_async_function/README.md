0x01. Python - Async

async, await, and asyncio are features in Python used for asynchronous programming, allowing you to write non-blocking and concurrent code, particularly useful in tasks like I/O-bound operations, network communication, and parallelism.

async and await:

async is a keyword used to define an asynchronous function. When you declare a function with async, it becomes a coroutine, which can be paused and resumed.
await is used inside asynchronous functions to pause execution until an asynchronous operation is completed. It's typically used with functions that return awaitable objects like coroutines, tasks, or Future objects.
Example of an asynchronous function using async and await:

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())
asyncio:

asyncio is a Python library that provides a framework for asynchronous programming. It allows you to manage and schedule asynchronous tasks (coroutines) and provides tools for concurrency and event-driven programming.
Key components of asyncio include the event loop, which schedules and runs tasks, and various utility functions for asynchronous I/O operations, like asyncio.sleep, asyncio.open_connection, and more.
Example of using asyncio to run asynchronous tasks:

import asyncio

async def foo():
    await asyncio.sleep(1)
    print("Foo")

async def bar():
    await asyncio.sleep(2)
    print("Bar")

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())
    await task1
    await task2

asyncio.run(main())
In the example above, asyncio.run(main()) starts the event loop and runs the asynchronous tasks concurrently.

Asynchronous programming can improve the performance of applications that spend a lot of time waiting for I/O operations by allowing other tasks to run while waiting. However, it's essential to understand its intricacies and handle potential concurrency issues carefully, such as race conditions and shared resources, to write robust asynchronous code.


random.uniform(a, b) is a function in Python's random module that generates a random floating-point number x such that a <= x <= b. In other words, it returns a random number within a specified range, where both the lower bound (a) and the upper bound (b) are inclusive.

Here's how you can use random.uniform:

import random

# Generate a random float between 0 and 1
random_float = random.uniform(0, 1)
print(random_float)

# Generate a random float between 10 and 20
random_range = random.uniform(10, 20)
print(random_range)
In the first example, random.uniform(0, 1) will generate a random float between 0 and 1, including both 0 and 1. The result can be any number in the range [0, 1].

In the second example, random.uniform(10, 20) will generate a random float between 10 and 20, including both 10 and 20. The result can be any number in the range [10, 20].

random.uniform is useful when you need random values that are not limited to integers and need to specify a range of possible values for your random number.
