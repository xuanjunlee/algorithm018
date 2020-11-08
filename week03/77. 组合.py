class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = list()

        def back_tracking(start_idx, path):
            if len(path) == k:
                ans.append(path)
                return

            for idx in range(start_idx, n-(k-len(path))+2):
                back_tracking(idx+1, path+[idx])


        back_tracking(1,list())
        return ans