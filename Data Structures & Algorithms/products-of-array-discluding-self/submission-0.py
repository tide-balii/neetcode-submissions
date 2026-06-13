class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnList = []
        for i in range(0, len(nums)): 
            product = 1
            for num in range(0, len(nums)): 
                if (num == i): 
                    continue 
                product = product * nums[num]
            returnList.append(product)
        return returnList

        