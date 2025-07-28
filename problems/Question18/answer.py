class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Modified Merge Sort Algorithm to find reverse pairs
        def mergesort(nums):
            if len(nums)<=1:
                return nums,0 # The Returned Array and Count of Reverse Pair

            mid = len(nums) // 2
            left,left_count = mergesort(nums[:mid])
            right,right_count = mergesort(nums[mid:])
            total = left_count+right_count

            #Reverse Pair Logic
            j=0
            for i in range(len(left)):
                while j<len(right) and left[i] > 2 * right[j]:
                    j+=1
                total+=j
        
            #Merge Sort Logic
            result = []
            i = j = 0

            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1

            while i<len(left):
                result.append(left[i])
                i+=1

            while j<len(right):
                result.append(right[j])
                j+=1

            return result,total
    
        res,cnt = mergesort(nums)
        return cnt
            

