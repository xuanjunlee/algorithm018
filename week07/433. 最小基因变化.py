from collections import defaultdict
from queue import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        cache = defaultdict(list)

        bank = set(bank)
        if start not in bank:
            bank.add(start)

        for item in bank:
            for idx in range(len(item)):
                temp_str = item[:idx] + '_' + item[idx + 1:]
                cache[temp_str].append(item)

        def bfs():
            que = deque()
            que.append(start)
            ans = 0
            used = set()

            while que:
                length = len(que)
                ans += 1

                for _ in range(length):
                    gene = que.popleft()

                    if gene == end:
                        return ans - 1

                    used.add(gene)

                    for idx in range(len(gene)):
                        temp_str = gene[:idx] + '_' + gene[idx + 1:]
                        for item in cache[temp_str]:
                            if item in used:
                                continue
                            que.append(item)

            return -1

        return bfs()

