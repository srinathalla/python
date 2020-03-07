from typing import List


class Solution:
    def maxLength(self, A: List[str]) -> int:
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in dp[:]:
                if a & c:
                    continue
                dp.append(a | c)
        return max(len(a) for a in dp)


s = Solution()
print(s.maxLength(["un", "iq", "ue"]))
