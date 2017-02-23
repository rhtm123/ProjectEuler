# -*- coding: utf-8 -*-
"""
ProjectEuler#55 using Python3

@author: Rohit Maurya
"""
def ispalindrome(n):
    rev = ''.join(reversed(str(n)))
    if str(n) == rev:
        return True
        
def isLychrel(n):
    n=n
    kuch = True
    for i in range(54):
        rev = ''.join(reversed(str(n)))
        n = n + int(rev)
        if ispalindrome(n):
            kuch = False
            break
    return kuch

if __name__=='__main__':
    count = 0
    for i in range(1,10000):
        if isLychrel(i):
            count = count+1
    print(count)
        
        
