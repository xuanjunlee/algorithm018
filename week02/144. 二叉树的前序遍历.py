from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        #递归法
        ans = list()

        def search(node):
            if not node:
                return

            ans.append(node.val)
            search(node.left)
            search(node.right)

        search(root)
        return ans

        #迭代法
        ans = list()
        stack = list()
        if not root:
            return list()

        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            if not node:
                continue

            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans
