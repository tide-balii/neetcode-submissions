class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        

        for i in range (len(prices)) : 
            for j in range (i+1, len(prices)) : 
                tempProfit = prices[j] - prices[i] 
                if tempProfit > maxProfit : 
                    maxProfit = tempProfit

        return maxProfit 
                