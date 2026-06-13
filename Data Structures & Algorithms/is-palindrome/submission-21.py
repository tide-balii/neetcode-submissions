class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s :
            if i.isalnum() :
                newS += i.lower()
        test = True 
        l = 0 
        r = len(newS) - 1 

        while r >= l and test:
            if newS[l] != newS[r] :
                test = False
            l += 1
            r -= 1 
        
        return test
