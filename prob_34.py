#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:50:34 2017

@author: fun
"""
from timeit import default_timer as timer
from math import factorial as fact
start = timer()

'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
'''

def sumoffact(n):
    sum = 0
    while n >0:
        a = int(n%10)
        sum =sum + fact(a)
        n = int(n/10)
    return sum

sum =0 
for i in range (11,600000):
    if sumoffact(i) == i:
        sum = sum +i
       
        
print(sum)

elapsed_time = (timer() - start) * 1000 # s --> ms

print(elapsed_time)