class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            if i + 1 == len(nums) : 
                break
            for y in range (i + 1, len(nums)):
                if (nums[i] + nums[y] == target):
                    return [i, y]

        return []