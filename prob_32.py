#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:34:21 2017

@author: #maurya
"""

def isPandigitalString(string):
    """ Check if string contains a pandigital number. """
    digits = len(string)

    if digits >= 10:
        return False

    for i in range(1,digits+1):
        if str(i) not in string:
            return False
    return True
    
def gives9PandigitalProduct(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return isPandigitalString(numbers)

products = []
for a in range(0, 99):
    for b in range(a, 9999):
        if len(str(a*b) + str(a) + str(b)) > 9:
            break
        if gives9PandigitalProduct(a, b):
            products.append(a*b)
            print("%i x %i = %i" % (a, b, a*b))

print(sum(set(products)))