from typing import List


class Solution:
    #
    # Naive Solution two loops T.C : O(n*n)
    # #
    # #
    def maxAreaNaive(self, height: List[int]) -> int:

        maxVal = float('-inf')
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                minHeight = min(height[i], height[j])
                maxVal = max(maxVal, minHeight * (j - i))

        return maxVal

    #
    # T.C : O(n) single pass solution using two pointers
    # #
    def maxArea(self, height: List[int]) -> int:

        maxVal = float('-inf')
        i = 0
        j = len(height) - 1

        while i < j:
            minHeight = min(height[i], height[j])
            maxVal = max(maxVal, minHeight * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxVal


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
