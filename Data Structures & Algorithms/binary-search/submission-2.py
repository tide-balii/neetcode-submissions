class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        midPoint = (left + right) // 2
        while left <= right : 
            midPoint = (left + right) // 2 
            if target > nums[midPoint] : 
                left = midPoint + 1
            
            elif target < nums[midPoint] : 
                right = midPoint - 1 
                
            else : 
               return midPoint 
            
        return -1
            