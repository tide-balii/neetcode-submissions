class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(start, currNumber, currArray) : 
            if currNumber == target : 
                res.append(list(currArray)) 

            elif currNumber > target : 
                return

            else : 
                for i in range(start, len(nums)) : 
                    choice = nums[i]
                    currArray.append(choice)
                    backtracking(i, currNumber + choice, currArray) 
                    currArray.pop()
            
        backtracking(0,0,[])
        return res