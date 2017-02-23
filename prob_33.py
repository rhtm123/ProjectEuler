#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:57:46 2017

@author: fun
"""

def str_array(n):
    a=[]
    while n > 0:
        kuch = n % 10
        
        a.append(kuch)
        n = n//10
    return a

nom = 1
de = 1
for i in range(11,99):
    for j in range(i+1,99):
        array1 = str_array(i)
        array2 = str_array(j)
        
        if array1[0]==0 or array2[0]==0 or array1[1]==0 or array2[1]==0:
            pass
        elif array1[1]==array2[1] and array1[0]/array2[0] == float(i/j):
            print("i1 %d and j %d"%(i,j))
            nom = i*nom
            de = j*de
        elif array1[1]==array2[0] and array1[0]/array2[1] == float(i/j):
            print("i2 %d and j %d"%(i,j))
            nom = i*nom
            de = j*de
        elif array1[0]==array2[1] and array1[1]/array2[0] == float(i/j):
            print("i3 %d and j %d"%(i,j))
            nom = i*nom
            de = j*de
        elif array1[0]==array2[0] and array1[1]/array2[1] == float(i/j):
            print("i4 %d and j %d"%(i,j))
            nom = i*nom
            de = j*de
        else :
            pass

#answer=100

print(int(de/nom))