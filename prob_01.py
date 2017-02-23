#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Rohit Maurya

from timeit import default_timer as timer

start = timer()
def check(n):
    if n%3==0 or n%5==0:
        return True

def main():
    sum = 0
    for i in range(1,1000):
        if check(i):
            sum = sum + i
    print(sum)
            
    
if __name__ == '__main__':
    main()
    
end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)