#Example 
arr = [3,1,3]

#Importing Hash Map
from collections import defaultdict

# Initialize variables
freq = defaultdict(int)
n = len(arr)

#Creating frequency map using hashmap
for num in arr:
    freq[num] +=1

# Basic Idea - repeating number has frequency of 2 and missing number  has frequency of 0
for i in range(1,n+1):
    if freq[i] == 2:
        repeating = i
    elif freq[i] == 0: 
        missing = i

print(repeating,missing)