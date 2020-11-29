class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        ans = 0

        for idx_1 in range(length):
            for idx_2 in range(idx_1, -1, -1):
                dp[idx_1][idx_2] = s[idx_1]==s[idx_2] and (idx_1-idx_2<=2 or dp[idx_1-1][idx_2+1])
                if dp[idx_1][idx_2]:
                    ans += 1

        return ans
