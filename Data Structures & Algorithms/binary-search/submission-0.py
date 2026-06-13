class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1 
        midpoint = (first + last) // 2 
        if nums[midpoint] == target : 
            return midpoint

        while nums[midpoint] != target and first < last :
            if target > nums[midpoint] and nums[midpoint + 1] != None : 
                first = midpoint + 1 
                midpoint = (first + last) // 2 

            else : 
                last = midpoint - 1 
                midpoint = (first + last) // 2 
        
        if nums[midpoint] == target :
            return midpoint 
        else :
            return -1


        
        