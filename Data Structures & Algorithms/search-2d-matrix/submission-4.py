class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)-1
        cols = len(matrix[0]) -1

        l, r = 0, rows
        while l <= r:
            mid = (l+r)// 2
            if target > matrix[mid][cols]:
                if mid<rows and target<matrix[mid+1][0]:
                    return False
                l = mid +1
            elif target < matrix[mid][0]:
                if mid>0 and target> matrix[mid-1][cols]:
                    return False
                r = mid -1
            else:
                break
        
        row = mid
        l, r = 0, cols
        while l<=r:
            mid = (l+r)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid -1
            else:
                l = mid +1
        print(row, mid)
        return False
        


            
                

        