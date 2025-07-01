class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Checking whether the number is negative or positive , if negative treat as positive
        sign = -1 if x<0 else 1
        x *= sign
        rev = 0

        while x!=0:
            if rev > (2**31 - 1) // 10:
                return 0
            digit = x % 10
            rev = (rev*10) + digit
            x = x//10
        
        #Return Back to original Sign
        return sign * rev

        