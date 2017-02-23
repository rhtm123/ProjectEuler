#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:45:45 2017

@author: fun
"""
from timeit import default_timer as timer

start = timer()
def panDigital(n):
    string = str(n)
    kuch = True
    for i in range(1,10):
        if str(i) not in string:
            kuch = False
    return kuch

a= []
for i in range (1,100000):
    sum = ''
    for j in range(1,10):
        string = str(i*j)
        sum = sum + string
        
        if len(sum) == 9:
            if panDigital(int(sum)):
                a.append(int(sum))
        elif len(sum) >9:
            
            break;
        else:
            pass

end = timer()
time_taken = (end-start)*1000

print(max(a))
print("Total time taken to run this program %d ms"%time_taken)