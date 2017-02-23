#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ProjectEuler#21 using Python
auther: Rohit Maurya
"""

def sumfactor(n):
    s = 0
    for i in range(1,int((n+2)/2)):
        if n%i == 0:
            s = s+i
    return s

a = []
for i in range(4,10000):
    if sumfactor(sumfactor(i)) == i and sumfactor(i) !=i:
        a.append(i)
        
print(sum(a))
