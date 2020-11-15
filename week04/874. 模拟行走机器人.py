class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        direction = 0
        row = col = 0
        ans = 0

        for num in commands:
            if num == -1:
                direction = (direction + 1) % 4
            elif num == -2:
                direction = (direction + 3) % 4
            else:
                add_r, add_c = directions[direction]
                for _ in range(num):
                    new_r, new_c = row + add_r, col + add_c
                    if (new_r, new_c) in obstacles:
                        break
                    row, col = new_r, new_c

            ans = max(ans, row ** 2 + col ** 2)

        return ans