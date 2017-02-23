
"""
ProjectEuler#40 using Python3

@author: Rohit Maurya
"""

num = 0
f = [1, 10, 100, 1000, 10000, 100000, 1000000]
a = []
for i in range(1, 250000):
    for digit in str(i):
        num += 1
        if num in f:
            a.append(digit)
        if len(str(num))>1000000:
            break
            
s = 1        
for j in a:
    b = int(j)
    s = s*b
print(s)
print(a)