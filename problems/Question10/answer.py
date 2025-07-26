class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Floyd's Hare and Tortoise Method [Fast and Slow pointer - cycle method]
        # Initialize variables
        slow = nums[0]
        fast = nums[0]

        #Find the Cycle 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #Find the number from the cycle
        slow = nums[0] # Initialize slow to first number to compare
        while fast!=slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow