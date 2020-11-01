from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法
        ans = list()

        def search(node):
            if not node:
                return

            search(node.left)
            ans.append(node.val)
            search(node.right)

        search(root)
        return ans

        # 迭代法
        ans = list()
        stack = list()
        if not root:
            return list()

        cur = root

        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                ans.append(node.val)

                cur = node.right

        return ans