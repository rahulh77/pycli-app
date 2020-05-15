import os
import requests  
import json
import time
import random
from requests.exceptions import HTTPError

NUM_JOBS = 10

def do_some_work(i):
    """Get book details using Google Books API (sequentially)"""
    sleeptime = random.randint(2,5)
    print(f"Task {i}: Sleeping for {sleeptime} seconds.")
    time.sleep(sleeptime)
    print(f"Task {i} completed")

def sync_job():
    start_time = time.time()
    for i in range(1, NUM_JOBS+1):
        do_some_work(i)
    end_time = time.time()
    print(f"Time Taken for {NUM_JOBS} jobs: ", time.strftime("%H:%M:%S", time.gmtime(end_time-start_time)))
    

def main():
    sync_job()
    
if __name__ == '__main__':
    main()