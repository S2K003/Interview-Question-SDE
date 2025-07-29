class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # Sort the Numbers
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-3):
            #Skip Duplicate
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                #Skip j Duplicate
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                #Two Pointer Method
                left = j+1
                right = n-1

                while left<right:

                    total = nums[left] + nums[right] + nums[i] + nums[j]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        #Skip Duplicate on Two Pointer Method
                        while left<right and nums[left] == nums[left+1]:
                            left+=1
                        while left<right and nums[right] == nums[right-1]:
                            right-=1
                        
                        left+=1
                        right-=1
                    
                    elif total < target:
                        left+=1
                    else:
                        right-=1

        return res