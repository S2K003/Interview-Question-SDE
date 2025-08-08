def max_len(arr):
    sum_map = {}
    max_len = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum == 0:
            max_len = i+1
        
        if current_sum in sum_map:
            max_len = max(max_len,i-sum_map[current_sum])
        else:
            sum_map[current_sum] = i
            
    return max_len


arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(max_len(arr))