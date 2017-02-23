#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:44:05 2017

@author: fun
"""

from timeit import default_timer as timer

start = timer()

def isPalindrome(n):
    string = str(n)
    l = len(string)
    is_palin = True
    for i in range(0,int(l/2)):
        if string[i] != string[l-i-1]:
            is_palin = False
            break
    return is_palin

def isBinPalin(n):
    b = bin(n)
    b = b[2:]
    if isPalindrome(b):
        return True
    else:
        return False


sum = 0
for i in range(1,1000000):
    if isPalindrome(i) and isBinPalin(i):
        sum = sum +i

print(sum)
    


end = timer()
time = (end-start)*1000
print("Your program run for %d ms"%time)