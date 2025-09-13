Python Solution

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res