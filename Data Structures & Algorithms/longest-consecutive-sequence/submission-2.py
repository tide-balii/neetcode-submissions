class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        sequenceArray = []

        for number in nums:
            tempArray = []
            tempArray.append(number)
            for i in range (1, len(nums) + 1):
                if number + i in hashSet:
                    tempArray.append(number + i)
                else :
                    break
            if (len(tempArray) > len(sequenceArray)):
                sequenceArray = tempArray
        
        return len(sequenceArray)
                    
           


            
            
        