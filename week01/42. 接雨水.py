from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        # 维护递减(等于)栈。用于记录每个值左边界
        length = len(height)
        if length < 3:
            return 0

        stack = list()
        ans = 0

        for idx, num in enumerate(height):
            if len(stack) == 0 or num <= height[stack[-1]]:
                stack.append(idx)
                continue

            while len(stack) > 0 and num > height[stack[-1]]:
                val = height[stack.pop()]
                if len(stack) == 0:
                    break
                w = idx - stack[-1] - 1
                h = min(num, height[stack[-1]]) - val
                ans += (w * h)

            stack.append(idx)

        return ans
