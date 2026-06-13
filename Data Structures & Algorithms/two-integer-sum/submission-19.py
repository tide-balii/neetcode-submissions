class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        res = []

        for i in range(len(nums)) :
            temp = target - nums[i] 
            if temp in hashMap :
                res = [hashMap[temp],i]
                return res 
            else :
                hashMap[nums[i]] = i 
        
        return res
