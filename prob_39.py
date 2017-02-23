#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:16:49 2017

@author: Rohit Maurya
"""
#This is not the best solution for this problem

from timeit import default_timer as timer
from math import sqrt
start = timer()

a = []
p = 1000
for s in range(5,p):
    for i in range(1,int(s)):
        for j in range(i,int(s/2)):
            k = sqrt(i**2+j**2)
            if k == s - i - j:
                a.append(s)
                

a.sort()
print(a)
end = timer()
time_taken=(end-start)*1000
print('Time taken to run this program: %d ms'%time_taken)