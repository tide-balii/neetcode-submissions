class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1 : 
            return 1
	    
        hashMap = {chr(code) : 0 for code in range(ord('A'), ord('Z') + 1)}
        highestFreq = 0	
        leftPointer = 0  
        res = 0 
	
	    
        for rightPointer in range(len(s)) : 
            currentChar = s[rightPointer]
            hashMap[currentChar] += 1
            highestFreq = max(highestFreq, hashMap.get(currentChar))
            while ((rightPointer - leftPointer) + 1) - highestFreq > k : 
                hashMap[s[leftPointer]] -= 1
                leftPointer += 1 
            res = max(res, rightPointer - leftPointer + 1)

        return res 


        

        
