class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = True
        if len(s) % 2 == 1 :
            return False
        
        for i in s :
            if i == "[" or i == "{" or i == "(" :
                stack.append(i)
            else :
                if len(stack) == 0 :
                    return False
                if i == "]" and stack.pop() != "[" :
                    return False 
                elif i == "}" and stack.pop() != "{" :
                    return False
                elif i == ")" and stack.pop() != "(":
                    return False
                
        if len(stack) != 0 :
            return False       
        return res
        