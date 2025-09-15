Python Solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq_map = {}
        for num in nums:
            freq_map[num] = 1+freq_map.get(num,0) 
        
        res = []
        for index,value in freq_map.items():
            if value > (n/3):
                res.append(index)
        return res

Java Solution

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer,Integer> mp = new HashMap<>();
        for(int num: nums) {
            mp.put(num, mp.getOrDefault(num, 0) + 1);
        }
        
        int threshold = nums.length / 3;
        List<Integer> res = new ArrayList<>();
        
        for (Map.Entry<Integer, Integer> entry : mp.entrySet()) {
            if (entry.getValue() > threshold) {
                res.add(entry.getKey()); 
            }
        }
        
        return res;
    }
}
