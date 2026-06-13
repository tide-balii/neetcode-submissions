class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        array = []
        array.append(prices[0])
        res = 0 

        for i in range (1, len(prices)) : 
            buy = min(array)
            tempProfit = prices[i] - buy
            res = max(res, tempProfit)
            array.append(prices[i])

        return res

                        
        
                

