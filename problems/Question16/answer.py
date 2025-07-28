class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #boyer moore algorithm - Modified 

        #If the nums list is empty
        if not nums:
            return []

        #Step 1 : Find upto 2 candidates
        count1,count2 = 0,0
        candidate1,candidate2 = None,None

        for num in nums:
            if candidate1 == num:
                count1+=1
            elif candidate2 == num:
                count2+=1
            elif count1==0:
                #Change candidate Reset Count to 1
                candidate1 = num
                count1 = 1
            elif count2==0:
                #Change candidate Reset Count to 1
                candidate2 = num
                count2 = 1
            else:
                count1-=1
                count2-=1

        #Verify Candidates
        result = []
        for c in (candidate1,candidate2):
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result