class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        hashMap = defaultdict(list)
        for i in range(1, len(prices)) : 
            hashMap = defaultdict(list)
            for j in range(i):
                hashMap[prices[j]].append(j)
            buy = min(hashMap.keys())
            tempProfit = prices[i] - buy
            res = max(tempProfit, res)      
        return res           
            
            

                