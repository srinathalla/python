class Solution:
    def baseNeg2(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))


s = Solution()
print(s.baseNeg2(2))
print(s.baseNeg2(3))
print(s.baseNeg2(4))
print(s.baseNeg2(5))
print(s.baseNeg2(6))
print(s.baseNeg2(7))
