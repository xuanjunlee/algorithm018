from queue import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(row, col):
            visited[row][col] = True

            que = deque()
            que.append((row, col))
            nonlocal rows
            nonlocal cols

            while len(que) > 0:
                r, c = que.popleft()

                for direction in directions:
                    new_r, new_c = r + direction[0], c + direction[1]

                    if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c] and grid[new_r][
                        new_c] == '1':
                        visited[new_r][new_c] = True
                        que.append((new_r, new_c))

        def dfs(row, col):
            nonlocal rows
            nonlocal cols
            if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] == '0':
                return

            visited[row][col] = True

            for direction in directions:
                new_r, new_c = row + direction[0], col + direction[1]
                dfs(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == '1':
                    ans += 1
                    # bfs(r,c)
                    dfs(r, c)

        return ans