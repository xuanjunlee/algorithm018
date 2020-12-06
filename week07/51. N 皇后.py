class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = list()
        chess_board = [['.' for _ in range(n)] for _ in range(n)]

        def is_valid(row, col):
            for r in range(row):
                if chess_board[r][col] == 'Q':
                    return False

            r,c = row-1, col-1
            while r >= 0 and c >= 0:
                if chess_board[r][c] == 'Q':
                    return False

                r -= 1
                c -= 1

            r,c = row-1, col+1
            while r >= 0 and c < n:
                if chess_board[r][c] == 'Q':
                    return False

                r -= 1
                c += 1

            return True


        def back_tracking(start_r):
            if start_r >= n:
                ans.append([''.join(item) for item in chess_board])
                return

            for col in range(n):
                if not is_valid(start_r, col):
                    continue

                chess_board[start_r][col] = 'Q'
                back_tracking(start_r+1)
                chess_board[start_r][col] = '.'

        back_tracking(0)
        return ans