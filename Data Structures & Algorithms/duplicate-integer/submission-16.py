class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): 
            point1 = nums[i] 
            for y in range (i+1, len(nums)):
                point2 = nums[y] 
                if (point1 == point2):
                    return True
        return False 