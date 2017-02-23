
"""
projectEuler#29 using python3
@auther: Rohit Maurya
"""

from timeit import default_timer as timer
start = timer()


if __name__ == '__main__':
    a = []
    for i in range(2,101):
        for j in range(2,101):
            a.append(i**j)
    s = set(a)
    l = len(s)
    print(l)
            



end = timer()

time_taken = (end-start)*1000

print("time taken to run this program: %d ms"%(time_taken))
