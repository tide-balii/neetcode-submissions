class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) : 
            return ""

        mapOfS = {}
        mapOfT = {}
        have = 0
        currString = [1, float("inf")] 
        l = 0 

        for elem in t : 
            mapOfT[elem] = mapOfT.get(elem, 0) + 1 

        need = len(mapOfT) 
    
        for r in range(len(s)): 
            if s[r] in mapOfT :
                mapOfS[s[r]] = mapOfS.get(s[r], 0) + 1 
                if mapOfS[s[r]] == mapOfT[s[r]] : 
                    have += 1 

            while have == need : 
                if s[l] in mapOfT : 
                    mapOfS[s[l]] -= 1 
                    if mapOfS[s[l]] < mapOfT[s[l]] : 
                        have -= 1 
                if have < need : 
                    currRange = r - l 
                    if currRange < (currString[1] - currString[0]) : 
                        currString[0] = l 
                        currString[1] = r 
                
                l += 1

        if currString[0] == 1 and currString[1] == float("inf") :
            return ""

        return s[currString[0] : currString[1] + 1]

            
 

                






        return res

