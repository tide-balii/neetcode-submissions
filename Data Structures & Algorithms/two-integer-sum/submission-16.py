class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate (nums) : 
            diff = target - num
            if diff in hashMap.keys():
                if i != hashMap[diff]:
                    return [hashMap[diff], i]  
            hashMap[num] = i

        return []
