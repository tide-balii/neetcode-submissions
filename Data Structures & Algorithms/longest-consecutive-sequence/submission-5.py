class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0 

        if len(nums) == 1 :
            return 1 
            
        hashSet = set()

        for i in nums : 
            hashSet.add(i)

        res = 1
        longestConsecutive = 1
        for i in nums :
            if i + 1 in hashSet :
                temp = i 
                while True : 
                    if temp + 1 in hashSet :
                        longestConsecutive += 1
                        temp += 1 
                        continue 
                    res = max(res, longestConsecutive)
                    longestConsecutive = 1
                    break 

        return res
            