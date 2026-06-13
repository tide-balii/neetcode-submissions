class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pfStack = []

        for i in tokens : 
            if i == "+":
                pop2 = pfStack.pop()
                pop1 = pfStack.pop()
                pfStack.append(pop1 + pop2)
        
            elif i == "-":
                pop2 = pfStack.pop()
                pop1 = pfStack.pop()
                pfStack.append(pop1 - pop2)

            elif i == "*":
                pop2 = pfStack.pop()
                pop1 = pfStack.pop()
                pfStack.append(pop1 * pop2)
            
            elif i == "/":
                pop2 = pfStack.pop()
                pop1 = pfStack.pop()
                pfStack.append(int(pop1 / pop2))

            else : 
                pfStack.append(int(i))

        return pfStack[-1] 

        