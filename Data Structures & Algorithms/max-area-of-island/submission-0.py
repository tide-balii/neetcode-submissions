from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        localArea = 0 
        maxArea = 0
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]

        for row in range(len(grid)) :
            for col in range(len(grid[row])) :
                if grid[row][col] == 0:
                    continue 
                if grid[row][col] == 1 and (row, col) not in visited :
                    localArea = 0 
                    visited.add((row,col))
                    q.append((row,col))
                    while q: 
                        localArea += 1 
                        currRow, currCol = q.popleft()
                        for nr, nc in directions :
                            nextRow = currRow + nr
                            nextCol = currCol + nc

                            if self.isValid(nextRow, nextCol, grid, visited) :
                                visited.add((nextRow, nextCol))
                                q.append((nextRow, nextCol)) 
                    maxArea = max(maxArea, localArea)
        
        return maxArea


    def isValid(self, row, col, grid, visited) :
        if row < 0 or row >= len(grid) :
            return False
        if col < 0 or col >= len(grid[0]) :
            return False
        if (row, col) in visited or grid[row][col] == 0 :
            return False
        return True
    