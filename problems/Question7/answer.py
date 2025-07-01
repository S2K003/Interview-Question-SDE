#Brute Force Method
def check_prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return True if count==2 else False

import math
#Optimized Method - Square Root Method
def check_prime_optimized(n):
    count = 0
    sqrt = int(math.sqrt(n))
    for i in range(1,sqrt+1):
        if n%i==0:
            count+=1
            #CounterPart - (n//i)
            if (n//i) !=i:
                count+=1
    return True if count ==2 else False

print(check_prime_optimized(7))