class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range (0, len(matrix)) : 
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i]) - 1] :
               l = 0 
               r = len(matrix[i]) - 1
               while l <= r : 
                midPoint = (l + r) // 2 
                if target == matrix[i][midPoint] : 
                    return True 
                elif target < matrix[i][midPoint] :
                    r = midPoint - 1 
                else : 
                    l = midPoint + 1
        return False 
            

            
            