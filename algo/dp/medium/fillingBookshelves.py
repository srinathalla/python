from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        dp = [0] * (len(books) + 1)
        dp[0] = 0

        for i in range(1, len(books) + 1):
            w, h = books[i-1]
            dp[i] = dp[i-1] + h
            for j in range(i-1, 0, -1):
                if w + books[j-1][0] > shelf_width:
                    break

                h = max(h, books[j-1][1])
                w += books[j-1][0]
                dp[i] = min(dp[i], dp[j-1] + h)

        return dp[len(books)]


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
w = 4

s = Solution()
print(s.minHeightShelves(books, w))
