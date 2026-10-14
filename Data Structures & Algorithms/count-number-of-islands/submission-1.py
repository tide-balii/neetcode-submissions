from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0

        q = deque()
        visited = set()
        directions =  [(1,0), (-1,0), (0,-1), (0,1)]
        numOfIslands = 0

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                currVertex = grid[i][j]
                if currVertex == '0' : 
                    continue 
                
                elif currVertex == '1' and (i,j) not in visited : 
                    q.append((i,j))
                    visited.add((i,j))
                    numOfIslands += 1 
                    while q : 
                        vertexRow, vertexCol = q.popleft()
                        for nr, nc in directions : 
                            nextRow = vertexRow + nr 
                            nextCol = vertexCol + nc 
                        
                            if self.isValid(grid, nextRow, nextCol, visited) :
                                q.append((nextRow,nextCol)) 
                                visited.add((nextRow,nextCol))
                            
                    
        
        return numOfIslands 

    def isValid(self, grid, row, col, visited) :
        if row < 0 or row >= len(grid) :
            return False
        elif col < 0 or col >= len(grid[row]) : 
            return False
        elif grid[row][col] == '0' or (row, col) in visited :
            return False
        return True

