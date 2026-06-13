class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 :
            return 0
        
        profit = 0

        for i in range(len(prices)) :
            for j in range(i+1, len(prices)) :
                if prices[i] > prices[j] :
                    continue
                profit = max(prices[j] - prices[i], profit)

        return profit
        