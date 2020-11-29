class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]

        for col in range(cols - 2, -1, -1):
            dp[rows - 1][col] = grid[rows - 1][col] + dp[rows - 1][col + 1]

        for row in range(rows - 2, -1, -1):
            dp[row][cols - 1] = grid[row][cols - 1] + dp[row + 1][cols - 1]

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                dp[row][col] = min(dp[row + 1][col], dp[row][col + 1]) + grid[row][col]

        return dp[0][0]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cache = dict()

        def dfs(row, col):
            if row >= rows or col >= cols:
                return float('inf')

            if row == rows-1 and col == cols-1:
                return grid[rows-1][cols-1]

            if (row, col) in cache:
                return cache[(row, col)]

            ret1 = dfs(row+1, col) + grid[row][col]
            ret2 = dfs(row, col+1) + grid[row][col]

            ret = min(ret1, ret2)
            cache[(row, col)] = ret
            return ret

        return dfs(0, 0)