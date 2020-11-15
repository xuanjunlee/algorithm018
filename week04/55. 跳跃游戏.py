class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if not nums:
            return False

        length = len(nums)
        if length == 1:
            return True

        end = length - 1

        for idx in range(length - 1, -1, -1):
            if idx + nums[idx] >= end:
                end = idx

        return end == 0