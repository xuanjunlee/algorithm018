from typing import List


# 方法1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length < 2:
            return None

        step = k % length
        if step == 0:
            return None

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, length - 1)
        reverse(0, step - 1)
        reverse(step, length - 1)


# 方法1
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length < 2:
            return None

        step = k % length
        if step == 0:
            return None

        idx = length - step

        nums[:] = nums[idx:] + nums[:idx]
