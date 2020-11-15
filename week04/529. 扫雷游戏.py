class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
            if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
            self.m,self.n = len(board), len(board[0])
            def check(i, j):
                cnt = 0
                for x,y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < self.m and 0 <= y < self.n and board[x][y]=='M':
                        cnt += 1
                return cnt    
            def dfs(i, j):
                cnt = check(i, j)
                if not cnt:
                    board[i][j] = 'B'
                    for x, y in direction:
                        x, y = x + i, y + j
                        if  0 <= x < self.m and 0 <= y < self.n and board[x][y]=='E': dfs(x, y)
                else: board[i][j] = str(cnt)
            dfs(click[0],click[1])
            return board