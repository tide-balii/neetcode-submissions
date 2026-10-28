class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return 0 
        elif len(s) == 1 : 
            return 1 
	
        hashSet = set() 
        res = 0 
        l = 0 

        for r in range(len(s)) : 
            if s[r] in hashSet : 
                while s[r] in hashSet : 
                    hashSet.remove(s[l]) 
                    l += 1
            
            hashSet.add(s[r]) 				

            res = max(res, r - l + 1) 
        return res 
