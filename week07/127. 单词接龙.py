from collections import defaultdict
from queue import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        cache = defaultdict(list)

        for word in wordList:
            for idx in range(len(word)):
                temp_str = f"{word[:idx]}_{word[idx + 1:]}"
                cache[temp_str].append(word)

        def bfs():
            ans = 0
            que = deque()
            used = set()
            que.append(beginWord)

            while que:
                length = len(que)
                ans += 1
                for _ in range(length):
                    word = que.popleft()

                    if word == endWord:
                        return ans

                    used.add(word)

                    for idx in range(len(word)):
                        temp_str = f"{word[:idx]}_{word[idx + 1:]}"
                        for item in cache[temp_str]:
                            if item in used:
                                continue

                            que.append(item)

            return 0

        return bfs()