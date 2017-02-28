# -*- coding: utf-8 -*-
"""
ProjectEuler#99 Using Python3

@author: Rohit Maurya
"""

from math import log

file = open('prob_99.txt')

contents = file.read().split()

a = []

for ln, line in enumerate(contents, start=1):
    b, e = line.split(',')
    v = int(e) * log(int(b)) 
    a.append(v)

print(a.index(max(a))+1)