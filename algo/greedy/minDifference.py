
class Solution:
    def minDifference(self, A):
        A.sort()
        N = len(A)

        if N <= 3:
            return 0
        take = N - 3
        return min(A[i+take - 1] - A[i] for i in range(N - take + 1))


s = Solution()
print(s.minDifference([20, 75, 82, 81, 95]))
