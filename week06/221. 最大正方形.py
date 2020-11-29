class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        if rows < 1:
            return 0

        cols = len(matrix[0])
        ans = 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            dp[row][0] = int(matrix[row][0])
            if dp[row][0] > ans:
                ans = dp[row][0]

        for col in range(cols):
            dp[0][col] = int(matrix[0][col])
            if dp[0][col] > ans:
                ans = dp[0][col]

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == '1':
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1

                if dp[row][col] > ans:
                    ans = dp[row][col]

        return ans*ans
