import math


class Solution:
    def nthUglyNumber(self, n: int, A: int, B: int, C: int) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def lcm(a, b):
            return (a*b) // gcd(a, b)

        l = 1
        h = 2 * 10**9

        while l < h:
            m = l + h >> 1
            cnt = m//a + m//b + m//c - \
                m//lcm(a, b) - m//lcm(b, c) - \
                m//lcm(c, a) + m//lcm(a, lcm(b, c))

            if cnt < n:
                l = m + 1
            else:
                h = m
        return l


n = 5
a = 2
b = 3
c = 3
s = Solution()
print(s.nthUglyNumber(n, a, b, c))
