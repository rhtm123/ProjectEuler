# -*- coding: utf-8 -*-
"""
ProjectEuler#53

@author: Rohit Maurya
"""

from math import factorial as fac

count = 0
for n in range(0,101):
    for r in range(0, n+1):
        a= (fac(n))/(fac(r)*fac(n-r))
        if a > 1000000:
            count = count +1
print(count)


            
