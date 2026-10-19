class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        candidates.sort()

        def backtracking(start, currNum, currArray) : 
            if currNum == target : 
                res.append(list(currArray)) 
            
            elif currNum > target : 
                return

            else : 
                for i in range(start, len(candidates)) : 
                    if i > start and candidates[i] == candidates[i - 1]: 
                        continue
                    choice = candidates[i] 
                    currArray.append(choice)
                    backtracking(i + 1, currNum + choice, currArray)
                    currArray.pop()

        backtracking(0, 0, [])
        return res