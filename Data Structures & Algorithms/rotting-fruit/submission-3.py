from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        numofFreshFruit = 0 
        res = 0
        directions = [(1,0), (-1,0), (0, -1), (0,1)]

        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == 2 : 
                    q.append((i,j)) 
                    visited.add((i,j))
                elif grid[i][j] == 1 : 
                    numofFreshFruit += 1 
        
        numofRotten = len(q)
        temp = 0 

        if numofFreshFruit == 0 : 
            return res 
        
        while q : 
            currRow, currCol = q.popleft()
            temp += 1 
            for nr, nc in directions : 
                nextRow = nr + currRow 
                nextCol = nc + currCol 
                if self.isValid(grid, visited, nextRow, nextCol) :
                    q.append((nextRow, nextCol))
                    visited.add((nextRow, nextCol))
                    numofFreshFruit -= 1 
            if temp == numofRotten and q : 
                numofRotten = len(q)
                res += 1 
                temp = 0
            
        if numofFreshFruit > 0 : 
            return -1
        
        return res
                

    def isValid(self, grid, visited, nextRow, nextCol) : 
        if nextRow < 0 or nextRow >= len(grid) : 
            return False
        if nextCol < 0 or nextCol >= len(grid[0]) : 
            return False

        if (nextRow, nextCol) in visited or grid[nextRow][nextCol] == 0 : 
            return False
        
        return True
                