#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:37:56 2017

@author: fun
"""
##Will Solve later
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
            break

        i += w
        w = 6 - w

    return True
    
def prime_list():
    L = []
    for i in range(2,40):
        if isprime(i):
            L.append(i)
    return L
L = prime_list()

a=[0,0,0,0]
def main():
    for p in range(3000,3500):
        if a[-1] - a[-2] == a[-2] -a[-3] == a[-3]- a[-4] ==1:
            print(a[-4],a[-3],a[-2],a[-1])
            break
        for i in L:
            ind = L.index(i)
            for j in L[ind:]:
                inde = L.index(j)
                for k in L[inde:]:
                    c = L.index(k)
                    for l in L[c:]:
                        
                        if i*j*k*l ==p:
                            a.append(p)
                        elif i*j*k*l >p:
                            break
        
if __name__ == '__main__':
    
    main()