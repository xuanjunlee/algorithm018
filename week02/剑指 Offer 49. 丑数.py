class Solution:
    def nthUglyNumber(self, n: int) -> int:

        a = b = c = 0
        dp = [1] * n

        for idx in range(1, n):
            temp_a, temp_b, temp_c = dp[a] * 2, dp[b] * 3, dp[c] * 5

            dp[idx] = min(temp_a, temp_b, temp_c)

            if dp[idx] == temp_a:
                a += 1

            if dp[idx] == temp_b:
                b += 1

            if dp[idx] == temp_c:
                c += 1

        return dp[-1]
