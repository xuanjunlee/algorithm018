class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        cache = dict()

        def back_tracking(start_idx):
            if start_idx >= length:
                return 1
            if start_idx in cache:
                return cache[start_idx]
            ret = 0
            for idx in range(start_idx, length):
                if 1 <= int(s[start_idx:idx + 1]) <= 26:
                    ret += back_tracking(idx + 1)
                else:
                    break
            cache[start_idx] = ret
            return ret

        return back_tracking(0)