class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        if not g or not s:
            return 0

        g.sort()
        s.sort()
        index = len(s) - 1
        ans = 0

        for idx in range(len(g) - 1, -1, -1):
            if index < 0:
                break

            if s[index] >= g[idx]:
                ans += 1
                index -= 1

        return ans