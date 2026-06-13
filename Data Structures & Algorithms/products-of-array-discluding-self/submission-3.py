class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2 : 
            return [nums[1], nums[0]]   

        product = 1
        res = [0 for i in range(len(nums))]

        if 0 in nums : 
            numOfZeros = 0 
            for num in nums:
                if num : 
                    product *= num
                else :
                    numOfZeros += 1
            
            if numOfZeros > 1 :
                return [0] * len(nums)

            else :
                res = [0] * len(nums)
                for i in range(len(nums)):
                    if nums[i] == 0 : 
                        res[i] = product


        else :
            for i in range (1, len(nums)) :
                product = product * nums[i]
            res[0] = product

            for i in range(1, len(nums)) :
                res[i] = int((product / nums[i]) * nums[i - 1]) 
                product = res[i]

        return res