class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in nums :
            if i in hashMap :
                hashMap[i] += 1 
            else :
                hashMap[i] = 1 
        
        res = []

        highest = 0
        curr = 0
        for j in range(k) :
            for i in hashMap :
                if hashMap[i] > highest and i not in res:
                    highest = hashMap[i]
                    curr = i
            
            res.append(curr)
            highest = 0
            curr = 0
                    
        return res