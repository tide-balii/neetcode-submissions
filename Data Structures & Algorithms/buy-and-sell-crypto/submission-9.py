class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 :
            return 0
        
        b, s = 0, 1
        profit = 0 

        while s < len(prices) :
            if prices[s] > prices[b] :
                profit = max(profit, prices[s] - prices[b])
                s += 1 
            else :
                b = s 
                s += 1
        
        return profit

        