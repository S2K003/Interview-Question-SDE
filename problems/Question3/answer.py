class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2 # Element before the last element for comparision

        #Find the first decreasing pair from the end
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        
        #Find the element that is greater than i
        if i>=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
    
            #Found the element now swap the element of i and j
            nums[i],nums[j] = nums[j],nums[i]

        #Now reverse the subarray from i+1 to end
        left = i+1
        right = n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
    