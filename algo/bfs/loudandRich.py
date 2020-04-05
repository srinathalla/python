from collections import defaultdict
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(quiet)
        g = defaultdict(set)

        for r in richer:
            g[r[1]].add(r[0])

        res = [None]*n
        visited = [False]*n

        def dfs(g, v, quiet, res, visited):

            if res[v] is not None:
                return res[v]

            visited[v] = True
            arr = [(quiet[v], v)]
            for av in g[v]:
                if visited[av] == False:
                    item = dfs(g, av, quiet, res, visited)
                    arr.append(item)
                else:
                    arr.append(res[av])

            arr.sort(key=lambda x: x[0])
            res[v] = arr[0]

            return arr[0]

        for i in range(n):
            if visited[i] == False:
                dfs(g, i, quiet, res, visited)
        return [v for q, v in res]


r = [[0, 1]]
q = [0, 1]
s = Solution()
print(s.loudAndRich(r, q))
