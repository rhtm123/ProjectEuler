
"""
projectEuler#28 using python3
@auther: Rohit Maurya
"""

# This code 


from timeit import default_timer as timer
start = timer()


def dsum(n):
    
    s1 = 0
    for i in range(n-2):
        s = (n-2*i)**2
        k = n-2*i-1
        for j in range(4):               
            s1 = s1 + s 
            if s <= 1:
                break
            s = s - k        
            print(s)
    
dsum(2)
      


end = timer()

time_taken = (end-start)*1000

print("time taken to run this program: %d ms"%(time_taken))
