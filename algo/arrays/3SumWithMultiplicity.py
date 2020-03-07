from typing import List


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:

        A.sort()

        i = 0
        count = 0
        while i < len(A) - 2:
            j = i + 1
            k = len(A) - 1

            while j < k:
                if A[i] + A[j] + A[k] == target:
                    count += 1
                    k -= 1
                elif A[i] + A[j] + A[k] > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        return count


A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
s = Solution()
print(s.threeSumMulti(A, target))
