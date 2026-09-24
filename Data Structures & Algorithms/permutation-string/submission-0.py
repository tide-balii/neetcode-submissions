class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1 
        sorteds1 = sorted(s1)
        while r < len(s2) :
            splice = sorted(s2[l : r + 1])
            if splice == sorteds1 :
                return True 
            else : 
                l += 1
                r += 1 

        return False 


