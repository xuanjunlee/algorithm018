from collections import defaultdict
from queue import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = defaultdict(list)

        for word in wordList:
            for idx in range(len(word)):
                tmp_str = word[:idx]+'_'+word[idx+1:]
                words[tmp_str].append(word)

        que = deque()
        que.append((beginWord,1))
        cache = set()

        while que:
            wd, step = que.popleft()
            if wd in cache:
                continue

            cache.add(wd)
            if wd == endWord:
                return step

            for idx in range(len(wd)):
                tmp_str = wd[:idx]+'_'+wd[idx+1:]
                for w in words[tmp_str]:
                    que.append((w, step+1))


        return 0