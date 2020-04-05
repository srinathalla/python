from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        visited = [[False] * len(grid[0]) for i in range(len(grid))]

        def path(i, j, p, visited):

            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and visited[i][j] == False:

                if grid[i][j] not in p:
                    return False

                visited[i][j] = True

                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return True

                if grid[i][j] == 1:
                    if path(i, j-1, visited, set([3, 5])) or path(i, j+1, visited, set([2, 4])):
                        return True

                if grid[i][j] == 2:
                    if path(i-1, j, visited, set([3, 6])) or path(i + 1, j, visited, set([5, 6])):
                        return True

                if grid[i][j] == 3:
                    if path(i, j-1, visited, set([3, 5])) or path(i + 1, j, visited, set([5, 6])):
                        return True

                if grid[i][j] == 4:
                    if path(i, j+1, visited, set(2, 4)) or path(i + 1, j, visited, set([5, 6])):
                        return True

                if grid[i][j] == 5:
                    if path(i, j-1, visited, set([3, 5])) or path(i - 1, j, visited, set([3, 6])):
                        return True
                if grid[i][j] == 6:
                    if path(i, j+1, visited, set([2, 4])) or path(i - 1, j, visited, set([3, 6])):
                        return True

            return False

        return path(0, 0, set([1, 2, 3, 4, 5, 6]), visited)


g = [[2, 4, 3], [6, 5, 2]]
s = Solution()
print(s.hasValidPath(g))
