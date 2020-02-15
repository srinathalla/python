from typing import List
import heapq


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        rows, cols = len(arr), len(arr[0])

        for i in range(1, rows):
            min1 = min(arr[i-1])
            j1 = arr[i-1].index(min1)

            min2 = min(x for j, x in enumerate(arr[i-1]) if j != j1)

            for j in range(cols):
                if arr[i-1][j] == min1:
                    arr[i][j] += min2
                else:
                    arr[i][j] += min1
        return min(arr[-1])

    def minFallingPathSum2(self, arr: List[List[int]]) -> int:

        rows, cols = len(arr), len(arr[0])

        for i in range(1, rows):
            min1, min2 = heapq.nsmallest(2, arr[i-1])

            for j in range(cols):
                if arr[i-1][j] == min1:
                    arr[i][j] += min2
                else:
                    arr[i][j] += min1
        return min(arr[-1])


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.minFallingPathSum2(m))
