class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        returnList = []
        
        for i, num in enumerate(nums): 
            hashMap[num] = i
        
        for i, num in enumerate (nums):
            diff = target - num
            if diff in hashMap.keys() and i != hashMap[diff]:
                returnList.append(i)
                returnList.append(hashMap[diff])
                return returnList


