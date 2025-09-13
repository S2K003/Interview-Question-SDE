Python Solution

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = {}
        for num in nums:
            freq_map[num] = 1+freq_map.get(num,0)

        heap = []
        res = []
        #Finding the Maximum Element by appending and poping into queue
        for key,value in freq_map.items():
            heapq.heappush(heap,(-value,key))
        
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res

        