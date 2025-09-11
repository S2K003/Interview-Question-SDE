Python Solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index,num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return index,num_map[complement]

            num_map[num] = index


Java Solution

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> mp = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int complement = target - nums[i];
            if (mp.containsKey(complement))
            {
                return new int[]{i,mp.get(complement)};
            }
            mp.put(nums[i],i);
        }
        return new int[]{};
    }
}