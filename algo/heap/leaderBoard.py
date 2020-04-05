from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.map = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.map[playerId] += score

    def top(self, K: int) -> int:

        pq = []

        for key in self.map:
            heapq.heappush(pq, (self.map[key], key))
            if len(pq) > K:
                heapq.heappop(pq)

        return sum([v for v, k in pq])

    def reset(self, playerId: int) -> None:
        self.map[playerId] = 0
