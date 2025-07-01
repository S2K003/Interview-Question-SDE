import math

def countDigits(n):
    count = 0
    while n>0:
        count+=1
        n = n//10
    return count

#print(countDigits(100))

def countDigits_Optimized(n):
    count = int(math.log10(n)+1)
    return count

print(countDigits_Optimized(100))