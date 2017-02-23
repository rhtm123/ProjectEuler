
"""
ProjectEuler#52

@author: Rohit Maurya
"""
from timeit import default_timer as timer

start = timer()

def check(n):
    if set(str(n)) ==set(str(2*n)) ==set(str(3*n))==set(str(4*n)) == set(str(5*n))==set(str(5*n)):
        return True

if __name__ == '__main__':
    for i in range(1,200000):
        if check(i):
            print(i)
            break

end = timer()
time_taken = (end-start)*1000

print('time taken to run to this program %d ms'%time_taken)