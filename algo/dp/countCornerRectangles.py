from typing import List


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:

        ans = 0
        for i in range(len(grid) - 1):
            for j in range(i + 1, len(grid)):
                counter = 0
                for k in range(len(grid[0])):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        counter += 1

                ans += counter * (counter-1)//2

        return ans


s = Solution()
matrix = [[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]
print(s.countCornerRectangles(matrix))
