from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7

        def kadane(arr):
            currSum = arr[0]
            maxSum = arr[0]
            for i in range(1, len(arr)):
                currSum = max(arr[i], arr[i] + currSum)
                maxSum = max(currSum, maxSum)
            return maxSum

        return ((k-2) * max(sum(arr), 0) + kadane(arr*2)) % mod if k > 1 else kadane(arr) % mod

    def kConcatenationMaxSumNaive(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7

        def kadane(arr):
            currSum = arr[0]
            maxSum = arr[0]
            for i in range(1, len(arr)):
                currSum = max(arr[i], arr[i] + currSum)
                maxSum = max(currSum, maxSum)
            return maxSum

        return kadane(arr * K) % mod


arr = [1, -2, 1]
k = 5
s = Solution()
print(s.kConcatenationMaxSum(arr, k))
