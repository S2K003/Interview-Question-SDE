class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Default Variables - min_price and max_profit 
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            #Finding the minimum price
            if price < min_price:
                min_price = price
            #Finding the maximum profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit