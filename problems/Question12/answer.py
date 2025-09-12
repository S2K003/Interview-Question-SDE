class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
            
        i=0
        for value,freq in freq_map.items():
            nums[i:i+freq] = [value] * freq
            i = i + freq
        return nums