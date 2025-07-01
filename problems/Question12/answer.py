#Frequency of Number
def frequency(arr):
    mp = {}
    for number in arr:
        if number not in mp:
            mp[number]=1
        else:
            mp[number]+=1
    print(mp)
    
frequency([1,2,2,3,3])