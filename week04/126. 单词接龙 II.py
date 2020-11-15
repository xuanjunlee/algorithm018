class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + "_" + word[i + 1:]
                wordDict[tmp].append(word)

        q = collections.defaultdict(list)
        q[beginWord].append([beginWord])
        visited, res = set(), []
        while len(q):
            nq = collections.defaultdict(list)
            for k, v in q.items():
                if k == endWord:
                    return v
                if k not in visited:
                    visited.add(k)
                    for i in range(len(k)):
                        tmp = k[:i] + "_" + k[i + 1:]
                        for neigh in wordDict[tmp]:
                            nq[neigh] += [j + [neigh] for j in v]  # 这里
            q = nq
        return res