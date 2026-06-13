class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)) :
            if nums[i] not in hashMap : 
                hashMap[nums[i]] = i
            temp = target - nums[i] 
            if temp in hashMap  :
                if hashMap[temp] != i :
                    return [hashMap[temp], i]

        return [0,0]