class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        time = 0
        fresh = 0
        visited = set()
        q = deque()

        def nextFruit(r, c):
            nonlocal fresh
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r, c) in visited:
                return
            fresh -=1
            visited.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh +=1
        
        while fresh>0 and q:
            qLen = len(q)
            time +=1
            for i in range(qLen):
                r, c = q.popleft()
                nextFruit(r+1, c)
                nextFruit(r-1, c)
                nextFruit(r, c+1)
                nextFruit(r, c-1)
            
        print(fresh)
        if fresh==0:
            return time
        return -1