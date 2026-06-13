class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashMap = {"+" : "+", "-" : "-", "*" : "*", "/" : "/"}
        pfStack = []

        for i in tokens : 
            if i in hashMap :
                if hashMap[i] == "+":
                    pop2 = pfStack.pop()
                    pop1 = pfStack.pop()
                    pfStack.append(pop1 + pop2)
            
                elif hashMap[i] == "-":
                    pop2 = pfStack.pop()
                    pop1 = pfStack.pop()
                    pfStack.append(pop1 - pop2)

                elif hashMap[i] == "*":
                    pop2 = pfStack.pop()
                    pop1 = pfStack.pop()
                    pfStack.append(pop1 * pop2)
                
                elif hashMap[i] == "/":
                    pop2 = pfStack.pop()
                    pop1 = pfStack.pop()
                    pfStack.append(int(pop1 / pop2))

            else : 
                pfStack.append(int(i))

        return pfStack[-1] 

        