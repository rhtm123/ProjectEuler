#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:19:00 2017

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
for i in range(10,1000):
    string = str(i)
    if isprime(i):
        for j in range(len(string)):
            if isprime(int(string[1:])) and isprime(int(string[-j:])):
                print(i)
            else:
                break
    
    
end = timer()
time_taken = (end-start)*1000
print("Total time taken to run this program %d ms"%time_taken)