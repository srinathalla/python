from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        left = [float('inf') for i in range(len(seats))]
        right = [float('inf') for i in range(len(seats))]

        oneIdx = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                oneIdx = i
            if seats[i] == 0:
                left[i] = i - oneIdx if oneIdx != -1 else left[i]

        oneIdx = -1
        for i in reversed(range(len(seats))):
            if seats[i] == 1:
                oneIdx = i
            if seats[i] == 0:
                right[i] = oneIdx - i if oneIdx != -1 else right[i]

        ans = float('-inf')
        for i in range(len(seats)):
            if seats[i] == 0:
                ans = max(ans, min(left[i], right[i]))

        return ans


s = Solution()
print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
print(s.maxDistToClosest([1, 0, 0, 0]))
