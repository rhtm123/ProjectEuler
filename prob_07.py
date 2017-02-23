# Project Euler Problem-7, python3
"""
@author: Rohit Maurya
"""

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
 

count = 0
for n in range(2, 1000000):
    if isprime(n):
        count = 1+ count
        if count == 10001:
            print(n)
            break

    
end = timer()
time_taken = (end-start)*1000
print("Time taken to run this program: %d ms"%time_taken)