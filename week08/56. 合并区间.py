class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        ans = list()

        for item in intervals:
            if not ans or ans[-1][1] < item[0]:
                ans.append(item)
                continue

            ans[-1][1] = max(item[1], ans[-1][1])

        return ans