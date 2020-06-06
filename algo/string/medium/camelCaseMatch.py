from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def match(q, p):
            j = 0
            for i in range(len(q)):
                if j < len(p) and q[i] == p[j]:
                    j += 1
                elif 65 <= ord(q[i]) <= 90:
                    return False

            return j == len(p)
        return [match(q, pattern) for q in queries]


s = Solution()
print(s.camelMatch(["FooBar", "FooBarTest", "FootBall",
                    "FrameBuffer", "ForceFeedBack"], "FB"))
