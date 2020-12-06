class DisjointSet(object):
    def __init__(self, num):
        self.num = [i for i in range(num)]

    def union(self, idx1, idx2):
        ret1 = self.parent(idx1)
        ret2 = self.parent(idx2)
        self.num[ret1] = ret2

    def parent(self, idx):
        root = idx

        while self.num[root] != root:
            root = self.num[root]

        while self.num[idx] != idx:
            idx, self.num[idx] = self.num[idx], root

        return root

    def search_parent(self, idx):
        root = idx

        while self.num[root] != root:
            root = self.num[root]

        return root


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        length = len(M)
        instance = DisjointSet(length)

        for row in range(length):
            for col in range(length):
                if M[row][col] == 0:
                    continue
                instance.union(row, col)

        return len(set(instance.parent(idx) for idx in range(length)))