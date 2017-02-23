# -*- coding: utf-8 -*-
"""
ProjectEuler#45 Using Python3
@auther: Rohit Maurya
"""

tri = set(n*(n+1)/2 for n in range(100000))
penta = set(n*(3*n-1)/2 for n in range(100000))

for n in range(100000):
    hexa = n*(2*n-1)
    if hexa in tri and hexa in penta and hexa>40755:
        print(hexa)
        break
