# -*- coding: utf-8 -*-
"""
ProjectEuler#56

@author: Rohit Maurya
"""
l = []
for i in range(60,100):
    for j in range(60,100):
        s = i**j
        l.append(s)

p = []        
for i in l:
    s = 0
    for k in str(i):
        s = s+ int(k)
    p.append(s)
print(max(p))
        