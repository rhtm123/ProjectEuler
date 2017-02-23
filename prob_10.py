

# Project Euler Problem-10 using python3

"""
@author: Rohit Maurya
"""

# This program does answer the question but takes some time.

from timeit import default_timer as timer

start = timer()

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
 

sum = 0
for n in range(2, 2000000):
    if isprime(n):
        sum = sum+n
print(sum)
    
end = timer()
time_taken = (end-start)*1000
print("Time taken to run this program: %d ms"%time_taken)