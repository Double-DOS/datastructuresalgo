class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        
        max_profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
                r = r+1
            else:
                l, r = r, r +1
        
        return max_profit