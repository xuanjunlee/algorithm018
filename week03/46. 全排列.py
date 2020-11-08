class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)
        ans = list()
        used = [False]*length

        def back_tracking(path):
            nonlocal length
            if len(path) == length:
                ans.append(path)
                return

            for idx,num in enumerate(nums):
                if used[idx]:
                    continue
                used[idx] = True
                back_tracking(path+[num])
                used[idx] = False

        back_tracking(list())
        return ans