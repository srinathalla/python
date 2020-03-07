from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        res = [a for a in A]
        l = 0
        h = len(A) - 1

        pairs = [(b, i) for i, b in enumerate(B)]
        pairs.sort(key=lambda x: x[0])

        while l <= h:
            pair = pairs.pop()
            if A[h] > pair[0]:
                res[pair[1]] = A[h]
                h -= 1
            else:
                res[pair[1]] = A[l]
                l += 1
        return res


A = [2, 7, 11, 15]
B = [1, 10, 4, 11]
s = Solution()
print(s.advantageCount(A, B))
