class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Create a set to avoid duplication
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if it is starting of sequence 
            if num-1 not in num_set:
                current = num
                streak = 1

                #Check if consecutive numbers are there in sets
                while current+1 in num_set:
                    current+=1
                    streak+=1
                
                longest = max(longest,streak)

        
        return longest