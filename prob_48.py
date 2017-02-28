#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:20:55 2017

@author: fun
"""
from timeit import default_timer as timer

start = timer()

s =0
for i in range(1,1000):
    s = s + i**i


print(s%10**10)

end = timer()
time_taken = (end-start)*1000
print('This program run for %d ms'%time_taken)

###The better Solution

