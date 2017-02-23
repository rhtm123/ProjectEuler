#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:16:31 2017

@author: fun
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

count =0
for i in range(2,1000000):
    if isprime(i):
        count = count +1
print(count)

end = timer()
time_taken = (end-start)*1000
print(time_taken)