class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i, visited):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r, c) in visited:
                return False
            
            
            if board[r][c] == word[i]:
                if i+1 == len(word):
                    return True
                visited.add((r, c))
                next = (dfs(r-1, c, i+1, visited) or dfs(r+1, c, i+1, visited) or dfs(r, c-1, i+1, visited) or dfs(r, c+1, i+1, visited))
                visited.remove((r, c))
                return next
            return False
        
        for i in range(ROWS):
            for j in range(COLS): 
                if dfs(i, j, 0, set()):
                    return True
        return False

                
