from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 方法1
        # cache用于记录值及其对应值的索引。遍历nums,如果值存在，则找到答案，如果不存在，
        # 记录该值对应的差值及该值索引

        cache = dict()

        for idx, num in enumerate(nums):
            if num in cache:
                return [cache.get(num), idx]

            cache[target - num] = idx
