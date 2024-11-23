# Time module in Python

# Time module is a set of functions to work with time-related operations.

# time.time() function returns time as a floating-point 
# representing the number of 'seconds' passed since the epoc(1 January 1970).

import time

def usingWhile():
    i=0
    while i<5000:
        i = i+1
        print(i)
        
def usingFor():
    for i in range(5000):
        print(i)
        
# time.time()
finit = time.time()     
usingFor()
fort = (time.time() - finit)

winit = time.time()     # the time passed since epoc
time.sleep(5)       #pause for given number of seconds
usingWhile()
print(time.time() - winit)  # seconds passed from winit to now to get he time taken by usingWhile to execute.
print(fort)

# time.sleep()
print(4)
time.sleep(3)
print(f"This print is executed 3 sec after previous line ")

# time.localtime()  -   gives local time in seconds
t = time.localtime()
# time.strftime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S%p , %A")
print(formatted_time)