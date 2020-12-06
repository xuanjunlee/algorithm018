class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def is_valid(row, col, num):
            for r in range(rows):
                if board[r][col] == num:
                    return False

            for c in range(cols):
                if board[row][c] == num:
                    return False

            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False

            return True

        def back_tracking():
            nonlocal rows, cols
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] != '.':
                        continue

                    for num in range(1, 10):
                        if not is_valid(row, col, str(num)):
                            continue

                        board[row][col] = str(num)
                        if back_tracking():
                            return True
                        board[row][col] = '.'

                    return False

            return True

        back_tracking()