from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:

        n = len(clips)

        dp = [T+1] * (T + 1)
        dp[0] = 0

        for i in range(1, T+1):
            for c in clips:
                if c[0] <= i <= c[1]:
                    dp[i] = min(dp[i], 1 + dp[c[0]])

        return -1 if dp[-1] == T + 1 else dp[-1]


clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
T = 10

s = Solution()
print(s.videoStitching(clips, T))
