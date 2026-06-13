class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in hashMap :
                return [hashMap[temp], i]

            hashMap[nums[i]] = i

        