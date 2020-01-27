from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return[newInterval]

        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        if newInterval[0] > intervals[len(intervals) - 1][1]:
            intervals.append(newInterval)
            return intervals

        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]),
                           max(intervals[i][1], newInterval[1])]
            i += 1

        result.append(newInterval)
        result.extend(intervals[i:])

        return result


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
s = Solution()
# res = s.insert(intervals, newInterval)
# print(res)


intervals = [[]]
newInterval = [4, 8]
# res = s.insert(intervals, newInterval)
# print(res)

intervals = [[1, 5]]
newInterval = [2, 3]
res = s.insert(intervals, newInterval)
print(res)
