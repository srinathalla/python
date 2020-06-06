import collections
from typing import List


class Solution:
    def constrainedSubsetSum(self, A: List[int], k: int) -> int:
        deque = collections.deque()
        for i in range(len(A)):
            A[i] += deque[0] if deque else 0
            while len(deque) and A[i] > deque[-1]:
                deque.pop()
            if A[i] > 0:
                deque.append(A[i])
            if i >= k and deque and deque[0] == A[i - k]:
                deque.popleft()
        return max(A)


#nums = [10, 2, -10, 5, 20]
nums = [-5, 4, -3, -2, -1]
k = 2

s = Solution()
print(s.constrainedSubsetSum(nums, k))
