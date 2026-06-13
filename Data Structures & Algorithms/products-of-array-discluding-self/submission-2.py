class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2 : 
            return [nums[1], nums[0]]   

        product = 1
        res = [0 for i in range(len(nums))]

        if 0 in nums : 
            for i in range(len(nums)) :
                if (nums[i] == 0) :
                    for j in range(len(nums)) : 
                        if (i != j) :
                            product = product * nums[j]
                    res[i] = product
                    product = 1 

        else :
            for i in range (1, len(nums)) :
                product = product * nums[i]
            res[0] = product

            for i in range(1, len(nums)) :
                res[i] = int((product / nums[i]) * nums[i - 1]) 
                product = res[i]

        return res