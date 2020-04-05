from typing import List
from collections import defaultdict


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        g = defaultdict(set)
        for s in synonyms:
            g[s[0]].add(s[1])
            g[s[1]].add(s[0])

        def dfs(g, m, v, c, clu):
            if v in m:
                return

            m[v] = c
            clu.append(v)
            for av in g[v]:
                dfs(g, m, av, c, clu)

        c = 0
        clu = []
        m = {}
        cl = []
        for w in g:
            if w not in m:
                dfs(g, m, w, c, clu)
                cl.append(clu[:])
                c += 1
                clu.clear()

        words = text.split()
        res = set()

        def prepare(words, idx):
            if idx == len(words):
                res.add(' '.join(words))
                return

            for i in range(idx, len(words)):
                if words[i] in m:
                    cid = m[words[i]]
                    for s in cl[cid]:
                        words[i] = s
                        prepare(words, i + 1)

            res.add(' '.join(words))

        prepare(words, 0)
        l = list(res)
        l.sort()
        return l


synonyms = [["a", "b"], ["c", "d"], ["e", "f"]]
text = "a c e"
s = Solution()
print(s.generateSentences(synonyms, text))
