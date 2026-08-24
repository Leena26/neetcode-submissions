class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def capture(r, c):
            if  r<0 or c<0 or r==row or c==col or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
            
        for r in range(row):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][col-1] == "O":
                capture(r, col-1)
        
        for c in range(col):
            if board[0][c]== "O":
                capture(0, c)
            if board[row-1][c]=="O":
                capture(row-1, c)
 
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"