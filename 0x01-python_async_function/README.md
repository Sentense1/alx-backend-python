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



0. The basics of async
mandatory
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 0-basic_async_syntax.py

1. Let's execute multiple coroutines at the same time with async
mandatory
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
The output for your answers might look a little different and that’s okay.

Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 1-concurrent_coroutines.py

2. Measure the runtime
mandatory
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.

bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 2-measure_runtime.py

3. Tasks
mandatory
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.

bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 3-tasks.py

4. Tasks
mandatory
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 4-tasks.py
