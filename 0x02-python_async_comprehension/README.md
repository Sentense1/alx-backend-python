0x02. Python - Async Comprehension

In Python, asynchronous comprehensions allow you to create asynchronous generators that produce a sequence of values asynchronously using the async for loop syntax. This feature is available in Python 3.6 and later versions. Async comprehensions are useful when you want to perform asynchronous operations inside a comprehension and collect the results asynchronously.

Here's the basic syntax of an asynchronous comprehension:

python
Copy code
async def main():
    result = [x async for x in async_generator()]
    print(result)

async def async_generator():
    # This is an example of an asynchronous generator function
    for i in range(5):
        await asyncio.sleep(1)
        yield i

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
In the example above:

async_generator is an asynchronous generator function that yields values with a delay of 1 second between each yield.

Inside the main coroutine, we use an asynchronous comprehension [x async for x in async_generator()] to iterate over the values produced by async_generator asynchronously. This means each value is awaited, and the loop doesn't block while waiting for the next value.

The asyncio.run(main()) call runs the main coroutine, which collects the values from the asynchronous comprehension and prints them when they are available.

Remember that you need to use an event loop like asyncio to run asynchronous code. In this example, we used asyncio.run() to run the main coroutine.

Async comprehensions can be particularly useful when working with asynchronous I/O operations, such as making HTTP requests or working with databases, where you want to efficiently collect results as they become available without blocking the event loop.




Tasks
0. Async Generator
mandatory
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
Repo:

GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 0-async_generator.py

1. Async Comprehensions
mandatory
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]

Repo:

GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 1-async_comprehension.py

2. Run time for four parallel comprehensions
mandatory
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135

Repo:

GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 2-measure_runtime.py
