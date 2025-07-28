class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        candidate = None 

        for num in nums:
            #Change the number if it becomes count is decremented to zero and there exists a new majority element
            if count == 0:
                candidate = num
                
            if num == candidate:
                count+=1
            else:
                count-=1
        
        return candidate