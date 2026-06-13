class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0 
        last = len(nums) - 1 
        midPoint = (first + last) // 2
        while nums[midPoint] != target and first < last : 
            if target > nums[midPoint] and nums[midPoint] + 1 != None : 
                first = midPoint + 1
                midPoint = (first + last) // 2 

            else : 
                last = midPoint - 1 
                midPoint = (first + last) // 2 
            
        

        if nums[midPoint] == target : 
            return midPoint 
        else : 
            return -1
            