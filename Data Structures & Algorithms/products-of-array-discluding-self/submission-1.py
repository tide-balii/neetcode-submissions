class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2 : 
            return [nums[1], nums[0]]

        res = [0 for i in range(len(nums))]
        for i in range(len(nums)) :
            product = 1
            for j in range(len(nums)) : 
                if i == j :
                    continue
                
                product = product * nums[j]
            
            res[i] = product


        return res
                
            
        