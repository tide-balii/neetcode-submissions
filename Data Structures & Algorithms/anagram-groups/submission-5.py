class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs :
            temp = str(sorted(i))
            if temp in hashMap :
                hashMap[temp].append(i)
            
            else :
                hashMap[temp] = [i]
                
        res = []

        for i in hashMap :
            res.append(hashMap[i])

        return res

        