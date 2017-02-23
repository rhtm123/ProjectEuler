#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:49:28 2017

@author: Rohit Maurya

"""
#this program does answer, but algo for this program sucks. 
 
from timeit import default_timer as timer

start = timer()

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
  
 
def similar(n,m):
    str_n = str(n)
    str_m = str(m)
    
    if sorted(str_n) == sorted(str_m):
        return True
    else: 
        return False
            

def main():
    
    """Main Program"""
    L = []
    for i in range(1000,9999):
        if isprime(i):
            L.append(i)
    diff = [0,0]
    l = [0,0,0]
    for i in L:
        for j in L:
            if j < i or j==i:
                pass
            else:
                if similar(i,j):
                    l.append(i)
                    l.append(j)
                    diff.append(j-i)
                    if diff[-1] == 2*diff[-2]:
                        print(l[-1],l[-2],l[-3])
                        break
        if diff[-1] == 2*diff[-2]:
            break
                    
if __name__ == '__main__':
    
    main()
   
end = timer()
time_taken = (end-start)*1000
print("Time taken to run this program:%d ms"%time_taken)