class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = []
        prev = intervals[0]

        for i in range(len(intervals)):
            curr = intervals[i]

            if prev[1] >= curr[0]:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
            else:
                res.append(prev)
                prev = curr

        res.append(prev)
        return res
