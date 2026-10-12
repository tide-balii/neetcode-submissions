from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        q = deque()
        res = 0

        movement = [(-1,0), (1,0), (0,1), (0, -1)] 

        for i in range(len(grid)) :
            for j in range (len(grid[i])) :
                if grid[i][j] == "0" : 
                    continue 
                if grid[i][j] == "1" and (i, j) not in visited :
                    q.append((i,j))
                    res += 1
                    visited.add((i,j))
                    while q :
                        currR, currC = q.popleft()

                        for nr, nc in movement : 
                            nextRow = currR + nr
                            nextCol = currC + nc 

                            if self.isValid(nextRow,nextCol,visited,grid) :
                                visited.add((nextRow, nextCol)) 
                                q.append((nextRow, nextCol))


        return res


    def isValid(self, row, col, visited, grid): 
        if row < 0 or row >= len(grid) :
            return False
        if col < 0 or col >= len(grid[row]) :
            return False
        if (row, col) in visited or grid[row][col] == "0" :
            return False
        return True