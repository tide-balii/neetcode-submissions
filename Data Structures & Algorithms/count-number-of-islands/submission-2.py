from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = deque()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        res = 0 

        for i in range(len(grid)) : 
            for j in range(len(grid[i])) : 
                if grid[i][j] == "1" and (i,j) not in visited : 
                    res += 1 
                    queue.append((i,j))
                    visited.add((i,j)) 

                    while queue : 
                        currRow, currCol = queue.popleft()
                        for nr, nc in directions : 
                            nextRow = nr + currRow 
                            nextCol = nc + currCol 
                        
                            if self.isValid(grid, nextRow, nextCol, visited) : 
                                visited.add((nextRow, nextCol))
                                queue.append((nextRow, nextCol))

        return res

    def isValid(self, grid, row, col, visited) : 
        if row < 0 or row >= len(grid) : 
            return False
        elif col < 0 or col >= len(grid[0]) : 
            return False
        elif grid[row][col] == "0" or (row, col)in visited :
            return False
        
        return True
