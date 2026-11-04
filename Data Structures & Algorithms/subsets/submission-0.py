class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = [] 
        res = []

        def backTracking(start) : 
            res.append(path[:])

            for i in range(start, len(nums)) :
                path.append(nums[i]) 
                backTracking(i + 1)
                path.pop()

        backTracking(0)
        return res 
