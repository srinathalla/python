import heapq


class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        sq = [[0]*sideLength for _ in range(sideLength)]

        for i in range(height):
            for j in range(width):
                sq[i % sideLength][j % sideLength] += 1
                print(sq)

        q = []
        for i in range(sideLength):
            for j in range(sideLength):
                heapq.heappush(q, -sq[i][j])

        count = 0
        for i in range(maxOnes):
            count += (-heapq.heappop(q))

        return count


s = Solution()

width = 3
height = 3
sideLength = 2
maxOnes = 2

print(s.maximumNumberOfOnes(width, height, sideLength, maxOnes))
