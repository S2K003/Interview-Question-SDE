class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Negative power condition - making it root of a number
        if n<0:
            n = -n
            x = 1/x

        #Loop condition - Until n becomes 0 
        result = 1
        while n:
            if n%2 == 1:
                result = result * x
            x *= x
            n //= 2

        return result