class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for idx in range(cols - 1, -1, -1):

            if obstacleGrid[rows - 1][idx] == 0:
                dp[rows - 1][idx] = 1
            else:
                break

        for idx in range(rows - 1, -1, -1):
            if obstacleGrid[idx][cols - 1] == 0:
                dp[idx][cols - 1] = 1
            else:
                break

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row + 1][col] + dp[row][col + 1]

        return dp[0][0]