from typing import List


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:

        g = {i: [] for i in range(1, N+1)}
        inDegree = [0] * (N+1)

        for r in relations:
            g[r[0]].append(r[1])
            inDegree[r[1]] += 1

        q = []
        semister = 0
        for i in range(1, N+1):
            if inDegree[i] == 0:
                q.append(i)

        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                p = q.pop(0)
                N -= 1
                adjV = g.get(p, None)
                if adjV is not None:
                    for adv in adjV:
                        inDegree[adv] -= 1
                        if inDegree[adv] == 0:
                            q.append(adv)

            semister += 1

        return semister if N == 0 else -1


N = 3
relations = [[1, 3], [2, 3]]
s = Solution()
print(s.minimumSemesters(N, relations))
print(s.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))
