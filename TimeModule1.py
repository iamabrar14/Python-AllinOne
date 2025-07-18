"""Time module in python provides functions to work with time
"""
import time
def usingwhile():
    i=0
    while i<5000:
        i=i+1
        print(i)
def usingfor():
    for i in range(5000):
        print(i)
        
init=time.time()
usingfor()
t1=time.time()-init
init=time.time()
usingwhile()
print(time.time()-init) #Will show execution time of while loop
print(t1)#Will show execution time of for loop
