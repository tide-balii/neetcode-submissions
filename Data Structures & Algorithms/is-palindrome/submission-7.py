class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s= s.strip()
        s = [char for char in s if char.isalnum()]
        s = ''.join(s)
        pointer2 = len(s) - 1 

        for i in range (len(s)):
            if s[i] != s[pointer2]:
                return False
            pointer2 -= 1
        
        return True





        