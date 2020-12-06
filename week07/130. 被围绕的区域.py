class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "O":
                return

            board[row][col] = "B"

            for direction in directions:
                dfs(row + direction[0], col + direction[1])

        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)

            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)

            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "B":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"