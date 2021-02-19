class Solution:
    def minimumSize(self, A: List[int], K: int) -> int:
        left, right = 1, max(A)
        while left < right:
            mid = left + right >> 1
            if sum((a-1)//mid for a in A) > K:
                left = mid + 1
            else:
                right = mid
        return left
