class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set() 
        left, right = 0,0 
        res = 0 

        while right < len(s) :
            if s[right] not in hashSet :
                hashSet.add(s[right])
                right += 1
                res = max(res, right - left)

            else : 
                while s[right] in hashSet :
                    hashSet.remove(s[left])
                    left += 1 
                 
                
        return res


