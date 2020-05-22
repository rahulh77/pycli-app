import os
import requests  
import json
import time
import random
import asyncio
from requests.exceptions import HTTPError

NUM_JOBS = 20

async def do_some_work_coro(i):
    """Does some work async"""
    sleeptime = random.randint(2,5)
    print(f"Task {i}: Sleeping for {sleeptime} seconds.")
    await asyncio.sleep(sleeptime)
    print(f"Task {i} completed after {sleeptime} seconds")

async def async_job():
    start_time = time.time()
    tasks = list()
    for i in range(1, NUM_JOBS+1):
        tasks.append(do_some_work_coro(i))
    
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Time Taken for {NUM_JOBS} jobs: ", time.strftime("%H:%M:%S", time.gmtime(end_time-start_time)))
    
def main():
    asyncio.run(async_job())
    
if __name__ == '__main__':
    main()