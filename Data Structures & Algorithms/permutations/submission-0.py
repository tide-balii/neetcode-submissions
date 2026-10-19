class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtracking(path, visited) : 
            if len(path) == len(nums) : 
                res.append(list(path))
                return
            
            for i in range(len(nums)) :
                if nums[i] in visited : 
                    continue
                
                choice = nums[i]
                path.append(choice)
                visited.add(choice)
                backtracking(path, visited) 

                path.pop()
                visited.remove(nums[i])

        backtracking([], visited)
        return res
