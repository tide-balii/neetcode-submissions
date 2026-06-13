class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum = prices[0]
        maxProfit = 0
        for i in range (1, len(prices)) :
            tempProfit = prices[i] - minNum
            maxProfit = max(maxProfit, tempProfit)
            minNum = min(prices[i], minNum)
        return maxProfit



           

            
        