import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #方法1
        dic = collections.Counter(nums)
        hp = list()

        count = 0
        for key,v in dic.items():
            if count < k:
                heapq.heappush(hp, (v,key))
            else:
                if v > hp[0][0]:
                    heapq.heappop(hp)
                    heapq.heappush(hp, (v,key))
            count += 1

        return [item[1] for item in hp][::-1]

        #方法2

        dic = collections.Counter(nums)
        hp = list()
        for key, v in dic.items():
            heapq.heappush(hp, (-1 * v, key))

        return [heapq.heappop(hp)[1] for _ in range(k)]
