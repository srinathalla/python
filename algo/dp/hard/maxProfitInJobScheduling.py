from typing import List
from functools import lru_cache


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time = list(zip(startTime, endTime, profit))
        time.sort()

        @lru_cache(None)
        def dfs(i):
            if i == len(time):
                return 0

            inc = 0
            inc += time[i][2]
            j = i + 1
            while j < len(time) and time[j][0] < time[i][1]:
                j += 1
            inc += dfs(j)

            exc = dfs(i+1)

            return max(inc, exc)

        return dfs(0)


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

s = Solution()
print(s.jobScheduling(startTime, endTime, profit))

startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]

print(s.jobScheduling(startTime, endTime, profit))

startTime = [1, 1, 1]
endTime = [2, 3, 4]
profit = [5, 6, 4]

print(s.jobScheduling(startTime, endTime, profit))
