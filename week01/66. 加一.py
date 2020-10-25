from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # 方法1：很有python风格的解法
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))

        # 方法2：数字小于9时，加1直接返回，等于9时，置0，继续判断下一位

        length = len(digits)
        for idx in range(length - 1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                return digits

            digits[idx] = 0

        return [1] + [0] * length
