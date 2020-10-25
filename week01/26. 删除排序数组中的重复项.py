class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        length = len(nums)

        if length < 2:
            return length

        first, second = 0, 1

        while second < length:
            if nums[first] == nums[second]:
                second += 1
                continue

            if second - first > 1:
                nums[first + 1] = nums[second]

            first += 1
            second += 1

        return first + 1
