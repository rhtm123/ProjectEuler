def numsum(n):
    sum = 0
    while n/10>0:
        sum = sum + (n%10)**5
        
        n = int(n/10)
        
    return sum

    

def kuchbhi():
    sum = 0
    for i in range(2,354294):
        if numsum(i) == i:
            sum = sum + i
            
    return sum
                        
print(kuchbhi())

