# -*- coding: utf-8 -*-
"""
ProjectEuler#63 using Python3

@author: Rohit Maurya
"""
count = 0
for i in range(555):
    for j in range(1,10):
        a = len(str(j**i))
        if a == i:
            count = count+1

print(count)