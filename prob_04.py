# projecteuler problem-4 using Python3
"""
Author: Rohit Maurya
"""

from timeit import default_timer as timer

start = timer()

def palindrome(n):
    sn = str(n)
    l = len(sn)
    kuch = True
    for i in range(int(l/2)):
        if sn[i] !=sn[l-i-1]:
            kuch = False
            break
    return kuch

print(palindrome(2345432))

l = []
def main():
    for i in range(101,999):
        for j in range(i,999):
            if palindrome(i*j):
                l.append(i*j)
    print(max(l))

    
    
if __name__ == '__main__':
    main()


end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)