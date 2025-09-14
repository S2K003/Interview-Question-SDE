Python Solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if price < buy_price: 
                buy_price = price 

            profit = max(profit , price-buy_price) 

        return profit

