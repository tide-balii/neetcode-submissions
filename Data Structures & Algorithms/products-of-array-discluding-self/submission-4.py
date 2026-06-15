class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        product = 1 
        for i in nums :
            if i == 0 :
                zeroCount += 1 
                if zeroCount == 1 :
                    continue 
                elif zeroCount >= 2 :
                    return [0 for i in range(len(nums))]
            product *= i

        res = []
        if zeroCount == 1 :
            for i in nums :
                if i == 0 :
                    res.append(product)
                else :
                    res.append(0)
        
        else :
            for i in nums :
                res.append(product//i)

        return res
        
        