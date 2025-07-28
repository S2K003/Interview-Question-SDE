class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Treat by using single dimensional matrix for dynamic programming
        dp = [1] * n

        for _ in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]

        return dp[-1] #Final Element - Total Ways 