class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range (len(temperatures)) : 
            counter = 0 
            for j in range (i, len(temperatures)) : 
                
                temp = temperatures[j]
                if temp > temperatures[i] : 
                    res.append(counter) 
                    break

                elif j == len(temperatures) - 1 and not temp > temperatures[i] : 
                    res.append(0)
                
                counter += 1
        return res

                

                
            


        