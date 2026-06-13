class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0] 
        res = 0 

        for i in range (1, len(prices)) : 
            tempProfit = prices[i] - minVal
            res = max(res, tempProfit)
            minVal = min(prices[i], minVal)

        return res

                        
        
                

