class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char.lower() for char in s if char.isalnum())
        if len(text) == 0 :
            return True
        if len(text) == 1 :
            return True 

        boolean = True 
        stop = 0 

        if len(s) % 2 == 0 :
            stop = len(s) / 2 
        else :
            stop = len(s) / 2 + 1 

        p1 = 0
        p2 = len(text) - 1 
        counter = 0 

        while boolean and counter < stop :
            if text[p1] != text[p2] :
                boolean = False

            p1 += 1 
            p2 -= 1
            counter += 1 

            if (p1 > p2) :
                return boolean

           
            
        return boolean
            

            