#Finding the Greatest Common Divisor
def find_gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a

n1 = 20
n2 = 15
gcd = find_gcd(n1, n2)
print(f"GCD of {n1} and {n2} is: {gcd}")