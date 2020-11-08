# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def divide_and_conquer(pre_nums, in_nums):
            if len(pre_nums) == 0 and len(in_nums) == 0:
                return None

            root = TreeNode(pre_nums[0])
            idx = in_nums.index(pre_nums[0])

            left = divide_and_conquer(pre_nums[1:idx+1], in_nums[:idx])
            right = divide_and_conquer(pre_nums[idx+1:], in_nums[idx+1:])

            root.left = left
            root.right = right

            return root

        return divide_and_conquer(preorder, inorder)