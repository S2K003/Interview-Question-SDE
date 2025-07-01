#Brute Force Method
def divisors(n):
    res = []
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

import math
#Optimized Method - Square Root Method
def divisors_optimized(n):
    res = []
    # Iterate upto SquareRoot of n
    sqrt = int(math.sqrt(n))
    
    for i in range(1,sqrt+1):
        if n%i==0:
            res.append(i)
            #Adding the counterpart if they are not the same number
            if i!=n//i:
                res.append(n//i)
    return res

print(divisors_optimized(36))
    