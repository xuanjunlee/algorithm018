class Solution:
    def longestValidParentheses(self, s: str) -> int:

        ans, stack = 0, list()

        for idx, ch in enumerate(s):
            if stack:
                if ch == ')' and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(idx)
            else:
                stack.append(idx)

            ans = max(ans, idx - stack[-1]) if stack else max(ans, idx + 1)

        return ans