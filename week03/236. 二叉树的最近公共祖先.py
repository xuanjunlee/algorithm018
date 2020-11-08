# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def back_tracking(node):

            if node == p or node == q or not node:
                return node

            left = back_tracking(node.left)
            right = back_tracking(node.right)

            if left and right:
                return node

            if left and not right:
                return left
            elif not left and right:
                return right
            else:
                return None

        return back_tracking(root)