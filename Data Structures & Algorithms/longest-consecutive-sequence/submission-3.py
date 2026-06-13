class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums) 
        res = 0 
        temp = 1 

        for i in sortedNums :
            tempNum = i  
            temp = 1 
            for j in sortedNums: 
                if tempNum + 1 in sortedNums:
                    temp += 1 
                    tempNum += 1
                else :
                    res = max(res, temp)
                    break

        return res
            

           

        