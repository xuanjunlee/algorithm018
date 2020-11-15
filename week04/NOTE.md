学习笔记

思路：即在数组中查找即小于左边又小于右边的数。但需要考虑该数在最左和最右的情况。
       当改变left和right的值时，应将mid考虑进去。

def binary_search(nums):
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = left+((right-left)>>1)
        
        if mid==0 and nums[mid]>nums[mid+1]:
            return mid
        if mid==len(nums)-1 and nums[mid]<nums[mid-1]:
            return mid
        if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
            return mid
        
        if nums[left] <= nums[mid]:
            if left == mid:
                left = mid+1
            else:
                left = mid
        else:
            if right == mid:
                left = mid-1
            else:
                right = mid