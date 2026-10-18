class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []
        safe = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for i in range(len(board)) :
            for j in range(len(board[0])) : 
                if i == 0 and board[i][j] == "O" : 
                    stack.append((i,j)) 
                    safe.add((i,j)) 
                elif i == len(board) - 1 and board[i][j] == "O" :  
                    stack.append((i,j))
                    safe.add((i,j))

                elif j == 0 and board[i][j] == "O" : 
                    stack.append((i,j))
                    safe.add((i,j))
                elif j == len(board[0]) - 1 and board[i][j] == "O" : 
                    stack.append((i,j))
                    safe.add((i,j))


        while stack : 
            currRow, currCol = stack.pop()
            for nr, nc in directions : 
                nextRow = currRow + nr 	
                nextCol = currCol + nc 
                if self.isValid(board, safe, nextRow, nextCol) : 
                    stack.append((nextRow, nextCol)) 
                    safe.add((nextRow, nextCol))

        for i in range(len(board)) : 
            for j in range(len(board[0])) :
                if (i,j) not in safe and board[i][j] == "O" : 
                    board[i][j] = "X"  

    def isValid(self, board, safe, row, col) : 
        if row < 0 or row >= len(board) : 
            return False
        if col < 0 or col >= len(board[0]) : 
            return False
        if (row, col) in safe or board[row][col] == "X" : 
            return False

        return True 
        





               