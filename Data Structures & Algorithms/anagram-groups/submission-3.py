class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) 
        res = []
        for i in strs :
            hashMap[tuple(sorted(i))].append(i) 

        for i in hashMap : 
            res.append(hashMap[i])

        return res 
            