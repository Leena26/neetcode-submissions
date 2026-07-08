class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        if row == 1:
            return target in matrix[0]
        
        
        top = 0
        bot = row-1
        #loop to find the row in which target can be
        while top <= bot:
            curr = (top + bot) // 2
            if target > matrix[curr][-1]:
                top = curr + 1
            elif target < matrix[curr][0]:
                bot = curr - 1
            else:
                break
        
        if not (top <= bot):
            return False
        curr = (top + bot) // 2
        return target in matrix[curr]

            
                

        