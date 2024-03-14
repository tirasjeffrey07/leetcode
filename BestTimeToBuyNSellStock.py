class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            # seeking lower buy value
            if buy > prices[i]:
                buy = prices[i]
            
            # seeking higher profit value
            elif buy - prices[i] > maxProfit:
                maxProfit = buy - prices[i]
            
        return maxProfit 



"""
optimised code:

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            # seeking higher profit value
            if price-buy > profit:
                profit = price-buy
            # seeking lower buy value
            elif price < buy:
                buy = price
        return profit
"""

        
                 
        