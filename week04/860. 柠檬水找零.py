from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        cache = defaultdict(int)

        for num in bills:
            if num == 5:
                cache[5] += 1
            elif num == 10:
                if cache[5] < 1:
                    return False

                cache[5] -= 1
                cache[10] += 1
            else:
                if cache[10] > 0 and cache[5] > 0:
                    cache[10] -= 1
                    cache[5] -= 1
                elif cache[10] < 1 and cache[5] > 2:
                    cache[5] -= 3
                else:
                    return False

        return True