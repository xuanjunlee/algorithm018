from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for item in strs:
            arr = [0] * 26
            for ch in item:
                arr[ord(ch) - ord('a')] += 1

            ans[tuple(arr)].append(item)

        return list(ans.values())
