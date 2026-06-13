class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []
        for i in nums : 
            if i not in hashMap :
                hashMap[i] = 1 
            else :
                hashMap[i] += 1

        for i in range(k) :
            mostFrequentNumber = -1001
            frequency = 0 
            for j in hashMap :
                if hashMap[j] > frequency and j not in res :
                    frequency = hashMap[j]
                    mostFrequentNumber = j
                
            res.append(mostFrequentNumber)
                


                

        


        
        return res
            
        
