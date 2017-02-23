#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:47:52 2017

@author: fun
"""
from timeit import default_timer as timer

start = timer()

# sum(n)=(n*(n+1))/2 and sum(n^2)= (n*(n+1)*(2n+1))/6
# or you can also by running for loop

n =100

sq_sum = (n*(n+1)*(2*n+1))/6
sum_sq = ((n*(n+1))/2)**2

print(sum_sq-sq_sum)


end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)