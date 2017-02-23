#project_euler problem#9 using python3.5

"""
@author: fun
"""

from timeit import default_timer as timer
start = timer()


# algo is designed by Juan Tolosa. Visit http://www.friesian.com/pythag.htm
'''
a = 2pq
b = p2 - q2
c = p2 + q2
'''

def main():
    for q in range(1,1000):
        for p in range(q,1000):
            if 2*p*(p+q) ==1000:
                a= 2*p*q
                b = p**2-q**2
                c = p**2+q**2
                print(a*b*c)
                break

if __name__ == '__main__':
    main()
            
end = timer()
time_taken = (end-start)*1000

print("Time taken to run this program: %d ms"%time_taken)