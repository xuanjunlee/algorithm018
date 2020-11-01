from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 方法1
        length1 = len(s)
        length2 = len(t)

        if length1 != length2:
            return False

        cache = defaultdict(int)

        for idx in range(length1):
            cache[s[idx]] += 1

        for idx in range(length1):
            cache[t[idx]] -= 1
            if cache[t[idx]] < 0:
                return False

        return not any(cache.values())
