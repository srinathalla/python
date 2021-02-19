from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        self.cycle = False

        def dfs(v, g, seen):
            if seen[v] is True:
                self.cycle = True
                return False

            seen[v] = True
            if v == destination:
                return len(g[v]) == 0

            found = False
            for nei in g[v]:
                found = dfs(nei, g, seen)

                if self.cycle is True:
                    return False

                if found:
                    break

            seen[v] = False
            return found

        g = {}
        for i in range(n):
            g[i] = set()

        for edge in edges:
            s, d = edge[0], edge[1]
            g[s].add(d)

        seen = [False] * n

        for v in g[source]:
            if dfs(v, g, seen) is False:
                return False

        return True


n = 3
edges = [[0, 1], [0, 2]]
source = 0
destination = 2

#s = Solution()
#print(s.leadsToDestination(n, edges, source, destination))


n = 4
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
source = 0
destination = 3

s = Solution()
print(s.leadsToDestination(n, edges, source, destination))
