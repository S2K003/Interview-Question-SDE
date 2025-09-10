Python Solution

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set()
        for num in nums:
            if num not in dup:
                dup.add(num)
            else:
                return True
        return False
        
Java Solution

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num:nums)
        {
            if(set.contains(num)==false)
            {
                set.add(num);
            }
            else
            {
                return true;
            }
        }
        return false;
    }
}