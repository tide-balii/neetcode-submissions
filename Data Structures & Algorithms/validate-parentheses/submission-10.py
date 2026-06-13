class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")" : "(", "}" : "{", "]" : "[" }
        stack = []
        for brac in s: 
            if brac in hashMap: 
                if stack and hashMap[brac] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else : 
                stack.append(brac)

        if not stack : 
            return True
        
        return False 
        


    

        