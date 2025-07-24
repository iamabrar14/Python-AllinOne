"""Function Caching is a technique for improving the performance of a program by storing the results
of a function call so that it can be use later.
"""
import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("Done for 20")    
print(fx(2))
print("Done for 2")    
print(fx(6))
#Same task, but this time it will not take 5 second because the result is already stored.
print("Done for 6")    
print(fx(20))
print("Done for 20")    
print(fx(2))
print("Done for 2")    
print(fx(6))
print("Done for 6")    