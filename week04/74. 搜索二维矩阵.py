class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows < 1:
            return False
        cols = len(matrix[0])
        if cols < 1:
            return False

        left, right = 0, rows*cols

        while left < right:
            mid = left + ((right-left)>>1)

            r = mid//cols
            c = mid%cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid+1
            else:
                right = mid

        return False