
Python Code
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums


Java Code
class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length;
        int[] temp = new int[2*len];
        for(int i=0;i<nums.length;i++)
        {
            temp[i] = nums[i];
            temp[i+len] = nums[i];
        }
        return temp;
    }
}

