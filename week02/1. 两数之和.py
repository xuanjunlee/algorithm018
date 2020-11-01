from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        if length < 2:
            return list()

        cache = dict()
        for idx in range(length):
            if nums[idx] in cache:
                return [idx, cache.get(nums[idx])]
            diff = target - nums[idx]
            cache[diff] = idx

        return list()
