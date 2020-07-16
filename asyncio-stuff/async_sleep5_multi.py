import asyncio
import random
import time
from functools import wraps, partial


NUM_JOBS = 5

# Wrapper to convert sync functions to async.
def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 




async def do_foo_work_coro(i):
    """Does some work async"""
    sleeptime = random.randint(2,5)
    print(f"FOO: Task {i}: Sleeping for {sleeptime} seconds.")
    await asyncio.sleep(sleeptime)
    print(f"FOO: Task {i} completed after {sleeptime} seconds")

async def do_bar_work_coro(i):
    """Does some work async"""
    sleeptime = random.randint(2,5)
    print(f"BAR: Task {i}: Sleeping for {sleeptime} seconds.")
    # await asyncio.sleep(sleeptime)
    async_sleep = async_wrap(time.sleep)
    await async_sleep(sleeptime)
    print(f"BAR: Task {i} completed after {sleeptime} seconds")

async def do_baz_work_coro(i):
    """Does some work async"""
    sleeptime = random.randint(2,5)
    print(f"BAZ: Task {i}: Sleeping for {sleeptime} seconds.")
    # await asyncio.sleep(sleeptime)
    async_sleep = async_wrap(time.sleep)
    await async_sleep(sleeptime)
    print(f"BAZ: Task {i} completed after {sleeptime} seconds")

async def async_job():
    start_time = time.time()
    tasks = list()
    for i in range(1, NUM_JOBS+1):
        tasks.append(do_foo_work_coro(i))
    # Run all foo tasks concurrently. Wait till all foo tasks are completed.
    await asyncio.gather(*tasks)

    tasks2 = list()
    for i in range(1, NUM_JOBS+1):
        tasks2.append(do_bar_work_coro(i))
    # Run all bar tasks concurrently. Wait till all foo tasks are completed.
    await asyncio.gather(*tasks2)
    # await asyncio.gather(*tasks, *tasks2)

    tasks3 = list()
    for i in range(1, NUM_JOBS+1):
        tasks3.append(do_baz_work_coro(i))
    # Run all baz tasks concurrently. Wait till all foo tasks are completed.
    await asyncio.gather(*tasks3)

    end_time = time.time()
    print(f"Time Taken for {NUM_JOBS} jobs: ", time.strftime("%H:%M:%S", time.gmtime(end_time-start_time)))
    
def main():
    asyncio.run(async_job())
    
if __name__ == '__main__':
    main()
