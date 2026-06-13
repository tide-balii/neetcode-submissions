class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return 0 
        
        if len(s) == 1 :
            return 1 
        
        hashSet = set()
        res = 0 
        temp = 0
        
        for i in range(len(s)) :
            for j in range(i, len(s)) :
                if s[j] not in hashSet :
                    hashSet.add(s[j])
                    temp += 1 
                    res = max(temp, res) 
                
                else :
                    temp = 0 
                    hashSet = set()
                    break
            
        return res


