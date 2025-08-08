def countSubarraysWithXOR(arr, K):
    xor_map = {}
    count = 0
    xor_sum = 0

    for num in arr:
        xor_sum ^= num

        if xor_sum == K:
            count += 1

        # If (xor_sum ^ K) has occurred before, add its frequency
        required_xor = xor_sum ^ K
        count += xor_map.get(required_xor, 0)

        # Update the frequency of xor_sum
        xor_map[xor_sum] = xor_map.get(xor_sum, 0) + 1

    return count
