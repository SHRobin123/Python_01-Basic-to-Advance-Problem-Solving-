#Async Programming Example

import asyncio

async def task1():
    for i in range(5):
        print("Task 1 running:", i)
        await asyncio.sleep(1)

async def task2():
    for i in range(5):
        print("Task 2 running:", i)
        await asyncio.sleep(1)

async def main():
    # running tasks concurrently
    await asyncio.gather(task1(), task2())

# running event loop
asyncio.run(main())

'''
output:-

Task 1 running: 0
Task 2 running: 0
Task 1 running: 1
Task 2 running: 1
Task 1 running: 2
Task 2 running: 2
Task 1 running: 3
Task 2 running: 3
Task 1 running: 4
Task 2 running: 4
'''