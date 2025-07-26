class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #Edge Case : If the interval list is empty
        if not intervals:
            return []

        #Sort the Intervals by start_time 
        intervals.sort(key= lambda x:x[0])

        #Result List
        merged = [intervals[0]]

        #Merger Logic
        for start,end in intervals:
            last_end = merged[-1][1] # End of previous element in result array

            #Check - if previous element's end is greater than current start then merge overlap
            if last_end >= start:
                merged[-1][1] = max(end,last_end)
            #If not overlapping 
            else:
                merged.append([start,end])
        
        return merged
