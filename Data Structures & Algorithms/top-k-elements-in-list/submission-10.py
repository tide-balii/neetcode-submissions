class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums : 
            if i not in hashMap : 
                hashMap[i] = 1 

            else :
                hashMap[i] += 1 
            
        
        res = []
        temp = []
        for i in hashMap :
            temp.append([i, hashMap[i]])

        temp.sort(key=lambda x:x[1], reverse=True)

        for i in range (k) :
            res.append(temp[i][0])

        return res
        