class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for i in strs :
            temp = "".join(sorted(i))
            hashMap[temp].append(i)
        
        res = []

        for i in hashMap :
            res.append(hashMap[i])    
                
        return res