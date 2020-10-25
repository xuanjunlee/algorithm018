from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法1：双指针：idx_0指向第一个为0的索引，idx_not_0只想idx_0后第一个不为0的索引
        idx_0, idx_not_0 = 0, 0
        length = len(nums)

        while True:

            while idx_0 < length and nums[idx_0] != 0:
                idx_0 += 1

            idx_not_0 = idx_0 + 1
            while idx_not_0 < length and nums[idx_not_0] == 0:
                idx_not_0 += 1

            if idx_0 >= length or idx_not_0 >= length:
                break

            nums[idx_0], nums[idx_not_0] = nums[idx_not_0], nums[idx_0]

        # 方法2：双指针，时间复杂度O(n)

        idx_0 = 0

        for idx, num in enumerate(nums):
            if num == 0:
                continue

            if idx_0 == idx:
                idx_0 += 1
                continue

            nums[idx_0] = num
            nums[idx] = 0
            idx_0 += 1
