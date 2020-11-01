from typing import List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        # 递归法
        ans= list()

        def search(node):
            if not node:
                return

            ans.append(node.val)

            if not node.children:
                return

            for item in node.children:
                search(item)

        search(root)
        return ans

        # 迭代法

        if not root:
            return list()

        ans = list()
        stack = list()
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            if not node:
                continue

            ans.append(node.val)

            if not node.children:
                continue

            for item in node.children[::-1]:
                stack.append(item)

        return ans