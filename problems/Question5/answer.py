class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0)
        
        count = 0
        for color,freq in map.items():
            nums[count:count+freq] = [color] * freq
            count += freq