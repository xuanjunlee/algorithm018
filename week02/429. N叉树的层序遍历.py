from queue import deque
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return list()

        ans = list()
        que = deque()
        que.append(root)

        while len(que) > 0:
            vals = list()
            length = len(que)

            for _ in range(length):
                node = que.popleft()
                vals.append(node.val)

                if not node.children:
                    continue

                for item in node.children:
                    que.append(item)

            ans.append(vals)

        return ans
