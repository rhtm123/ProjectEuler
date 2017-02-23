#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author : Rohit Maurya
"""

# This program takes more time than expected.I Will code sometime later.  

from math import sqrt
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
# Any composite number must have a factor below its square root.
    while i * i <= n:    
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

#print(sqrt(600851475143)) Ans: 775146
def prime_list():
    """Create prime number list below 1000000"""
    L = []
    for n in range(1, 800000):
        if isprime(n):
            L.append(n)
    return L



def main():
    primes = prime_list()
    n = 600851475143
    l = []
    for i in primes:
        if n%i == 0:
            l.append(i)

    print(l[-1])

    
if __name__ == '__main__':
    main()
  
end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)