from typing import List
import collections
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(set)
        for conn in connections:
            g[conn[0]].add(conn[1])
            g[conn[1]].add(conn[0])

        n = len(g.keys())
        connections = set(map(tuple, map(sorted, connections)))
        rank = [-2] * n

        def dfs(g, v, depth):

            if rank[v] >= 0:
                return rank[v]

            rank[v] = depth

            min_back_depth = n
            for av in g[v]:
                if rank[av] == depth - 1:
                    continue

                back_depth = dfs(g, av, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((v, av))))

                min_back_depth = min(min_back_depth, back_depth)

            return min_back_depth

        dfs(g, 0, 0)
        return list(connections)


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(list(map(tuple, [[2, 1]])))
s = Solution()
print(s.criticalConnections(4, connections))
