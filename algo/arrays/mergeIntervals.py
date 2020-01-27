from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 1:
            return intervals
        intervals.sort(key=lambda interval: interval[0])

        prev = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] >= curr[0]:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
            else:
                result.append(prev)
                prev = curr

        result.append(prev)
        return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

s = Solution()
res = s.merge(intervals)
print(res)

intervals = [[1, 4], [0, 0]]

s = Solution()
res = s.merge(intervals)
print(res)
