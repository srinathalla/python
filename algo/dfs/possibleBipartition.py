from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        g = {}
        for i in range(1, N+1):
            g[i] = []
        for dl in dislikes:
            g[dl[0]].append(dl[1])
            g[dl[1]].append(dl[0])

        group = [0] * (N + 1)

        def dfs(g, group, v, value):
            group[v] = value
            for av in g[v]:
                if group[av] == value:
                    return False

                if group[av] == 0 and dfs(g, group, av, -value) == False:
                    return False

            return True

        for i in range(1, N+1):
            if group[i] == 0 and dfs(g, group, i, 1) == False:
                return False
        return True


N = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
s = Solution()
print(s.possibleBipartition(N, dislikes))
