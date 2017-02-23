
"""
ProjectEuler#44 using Python
@author: Rohit Maurya
"""

from timeit import default_timer as timer


from itertools import product

start = timer()

penta_set= set(int(n*(3*n-1)/2) for n in range(1,3000))


for a,b in product(penta_set,penta_set):
    if a+b in penta_set and a-b in penta_set:
        print(abs(a-b))
        break
  
end = timer()
time_taken = (end-start)*1000

print('time taken to run to this program %d ms'%time_taken)