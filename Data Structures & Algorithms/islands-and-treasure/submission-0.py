from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [(1,0), (-1, 0), (0, -1), (0,1)]

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :
                    q.append((i,j))

        while q : 
            currRow, currCol = q.popleft()
            for nr, nc in directions :
                nextRow = nr + currRow
                nextCol = nc + currCol 
                if self.isValid(grid, nextRow, nextCol) :
                    grid[nextRow][nextCol] = grid[currRow][currCol] + 1
                    q.append((nextRow, nextCol))


    def isValid(self,grid, nextRow, nextCol) : 
        if nextRow < 0 or nextRow >= len(grid) :
            return False
        if nextCol < 0 or nextCol >= len(grid[0]) :
            return False
        if grid[nextRow][nextCol] != 2147483647 : 
            return False
        return True
