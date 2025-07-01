# Normal Method
def Armstrong(n):
    stored = n
    count_of_digits = 0
    temp = n
    while temp>0:
        count_of_digits +=1
        temp=temp//10
    arm = 0 
    while n>0:
        x =  n % 10
        arm = arm + (x**count_of_digits)
        n=n//10
    return True if stored == arm else False

#Optimal Method
def Optimized_armstrong(n):
    
    #Convert the number to string
    string = str(n)
    count_of_digits = len(string)
    arm = 0
    for number in string:
        arm += int(number)**count_of_digits 
    return True if arm == n else False
        
print(Optimized_armstrong(9474))
        