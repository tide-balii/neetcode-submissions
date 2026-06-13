class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(list)
        result = []
        for i in nums: 
            hashMap[i].append(i)
        
        
        for i in range (0, k):
            countTuple = [0,0] 
            for num, lists in hashMap.items(): 
                if (len(lists) > countTuple[1]):
                    countTuple[0] = num
                    countTuple[1] = len(lists)
            del hashMap[countTuple[0]]
            result.append(countTuple[0])     


        return result  


        