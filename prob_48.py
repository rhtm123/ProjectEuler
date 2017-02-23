#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:20:55 2017

@author: fun
"""
from timeit import default_timer as timer

start = timer()

sum =0
for i in range(1,1000):
    sum = sum + i**i

str_sum = str(sum)
l = len(str_sum)
last_ten = str_sum[l-10:l]
print(last_ten)

end = timer()
time_taken = (end-start)*1000
print('This program run for %d ms'%time_taken)