class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + ((right-left)>>1)

            if nums[mid] == target:
                return mid


            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid-1


        return -1