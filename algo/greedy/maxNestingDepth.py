from typing import List


class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        groups = []
        d = 0
        for c in s:
            open = c == '('
            if open:
                d += 1
            # group determined through parity (odd/even?) of depth
            groups.append(d % 2)
            if not open:
                d -= 1

        return groups


s = Solution()
print(s.maxDepthAfterSplit("(()())"))
