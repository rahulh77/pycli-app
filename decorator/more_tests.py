import typing
import time
import random


# decorator to calculate duration 
# taken by any function. 
def calculate_time(func): 
      
    # added arguments inside the inner1, 
    # if function takes any arguments, 
    # can be added like this. 
    def inner(*args, **kwargs): 
        # storing time before function execution 
        begin = time.time() 
        func(*args, **kwargs) 
        # storing time after function execution 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 
  
    return inner

def toupper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return inner
        

@calculate_time
def myfunc(input_str: str) -> str:
    sleeptime = random.randint(5,10)
    print(sleeptime)
    time.sleep(sleeptime)
    print(input_str)
    return input_str

@toupper
def myfunc2(input_str: str) -> str:
    return input_str

def mismatched_words(string1, string2):
    set_string1 = set(string1.split())
    set_string2 = set(string2.split())
    result = list(set_string1 - set_string2) + list(set_string2 - set_string1)
    # result = set_string1 ^ set_string2
    print (result)
    return result

if __name__ == "__main__":
    print(myfunc2('RaHuL'))
    myfunc('rahul')

    # mismatched_words('My name is Rahul', 'What is your name')