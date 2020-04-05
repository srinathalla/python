from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        bc = Counter("balloon")
        tc = Counter(text)

        res = 0
        while bc == (tc & bc):
            res += 1
            tc = tc - bc
        return res


text = "nlaebolko"
s = Solution()
print(s.maxNumberOfBalloons(text))
