class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s : 
            if i == "(" or i == "{" or i == "[" : 
                stack.append(i) 
            else :
                if i == ")" and stack:
                    if stack[-1] == "(" : 
                        stack.pop() 
                    else :
                        return False
                elif i == "]" and stack :
                    if stack[-1] == "[" : 
                        stack.pop() 
                    else :
                        return False
                elif i == "}" and stack :
                    if stack[-1] == "{" : 
                        stack.pop()
                    else :
                        return False
                else :
                    return False
        if stack :
            return False
        return True  

                    

                
            
        