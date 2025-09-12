Python Solution

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Frequency Map 
        freq_map = {}
        for num in nums:
            freq_map[num] = 1+freq_map.get(num,0)
        #Setting Threshold
        threshold = len(nums)//2
        #Finding the Value
        for value, freq in freq_map.items():
            if freq>threshold:
                return value
        return 0 
        

Java Solution

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> mp = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            mp.put(nums[i],mp.getOrDefault(nums[i],0)+1);
        }
        int threshold = (nums.length/2);
        for (Map.Entry<Integer, Integer> entry : mp.entrySet()) 
        {
            if (entry.getValue() > threshold) {
                return entry.getKey();
            }
        }
        return 0;
    }
}