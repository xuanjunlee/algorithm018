class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge_sort(left, right):
            print(left, right)
            if left >= right:
                return 0

            mid = left + ((right-left)>>1)

            ans = merge_sort(left, mid) + merge_sort(mid+1, right)

            temp_nums = list()
            idx_1 = idx_2 = left

            for idx in range(mid+1, right+1):
                while idx_1 <= mid and nums[idx_1] <= 2*nums[idx]:
                    idx_1 += 1

                while idx_2 <= mid and nums[idx_2] < nums[idx]:
                    temp_nums.append(nums[idx_2])
                    idx_2 += 1

                temp_nums.append(nums[idx])
                ans += mid-idx_1+1

            temp_nums.extend(nums[idx_2: mid+1])
            nums[left: right+1] = temp_nums

            return ans

        if not nums:
            return 0

        return merge_sort(0, len(nums)-1)



