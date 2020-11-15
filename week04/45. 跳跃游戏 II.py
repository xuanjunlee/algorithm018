class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt = 0
        max_ind = 0
        ind = 0
        while max_ind < len(nums) - 1:
            temp = []
            while ind <= max_ind:
                temp.append(ind + nums[ind])
                ind += 1
            max_ind = max(temp)
            cnt += 1
        return cnt