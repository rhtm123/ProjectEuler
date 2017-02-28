# -*- coding: utf-8 -*-
"""
ProjectEuler#57
@author: Rohit Maurya
"""

from fractions import Fraction as frac
from math import log10

'''
def kuch(n):
    if n==1:
        return frac(1,2)
    else:
        return frac(1,(2+kuch(n-1)))
'''

# 3/2, 7/5, 17/12, 41/29, 
# observe closely there is a relation 
count = 0

nm=3   # numerator
dm=2   # denominator

for i in range(2,1001):
    nm,dm = nm+2*dm, nm+dm
    if int(log10(nm))>int(log10(dm)):        
        count = count+1
    
print(count)
