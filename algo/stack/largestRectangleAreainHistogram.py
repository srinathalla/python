from typing import List


class Solution:

    def largestackRectangleArea(self, heights: List[int]) -> int:

        stack = [-1]
        n = len(heights)
        maxH = 0
        for i in range(len(heights)):

            while len(stack) > 1 and heights[stack[-1]] >= heights[i]:
                maxH = max(maxH, heights[stack.pop()] * (i-1 - stack[-1]))
            stack.append(i)

        while len(stack) > 1:
            maxH = max(maxH, heights[stack.pop()] * (n-1 - stack[-1]))

        return maxH


s = Solution()
print(s.largestackRectangleArea([2, 3]))
