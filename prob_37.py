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
    if n==1:
        return False
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
    


print(isprime(3331))
count =0
a =[]
for i in range(10,1000000):
    string = str(i)
    kuch = True
    if isprime(i):
        for j in range(1,len(string)):
            # Solution will be faster if we use % and / instead of int(string)
            a1 = int(string[j:])
            a2 = int(string[:j])
            if not isprime(a1) or not isprime(a2):
                kuch = False
                break
        if kuch:
            count = count+1
            a.append(i)
    if count ==11:
        break
print(sum(a))
        
            
    
    
end = timer()
time_taken = (end-start)*1000
print("Total time taken to run this program %d ms"%time_taken)