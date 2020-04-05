from typing import List
import collections


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count = collections.Counter(barcodes)

        res = [0] * len(barcodes)
        i = 0
        for a, v in count.most_common():
            for _ in range(v):
                res[i] = a
                i += 2

                if i >= len(barcodes):
                    i = 1

        return res


s = Solution()
print(s.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
