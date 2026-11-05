class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backTracking(index, sumSoFar, path) :
            if sumSoFar == target : 
                res.append(path[:]) 
                return
                
            if sumSoFar > target : 
                return 
            
            for i in range(index, len(nums)) : 
                path.append(nums[i]) 
                backTracking(i, sumSoFar + nums[i], path)
                path.pop() 

        backTracking(0,0,[])

        return res



