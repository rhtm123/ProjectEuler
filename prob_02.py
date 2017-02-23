#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Rohit Maurya

from timeit import default_timer as timer

start = timer()


L = [1]
sum= 1

for i in range(1000):
    sum = sum + L[i-1]
    
    if sum > 4000000:
        break
    L.append(sum)


def main():
    sum = 0
    for i in L:
        if i%2 ==0:
            sum = sum+i
    print(sum)
            

            
    
if __name__ == '__main__':
    main()
    
end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)