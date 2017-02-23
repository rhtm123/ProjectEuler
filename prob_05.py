# projecteuler problem-5 using Python3
"""
Author: Rohit Maurya
"""

from timeit import default_timer as timer

start = timer()

a= (2**4)*3*3*5*7*11*13*17*19
print(a)

end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)