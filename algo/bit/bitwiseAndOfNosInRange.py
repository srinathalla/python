class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        while n > m:
            n -= (n & -n)

        return n


m = 0
n = 2147483647

print(4 & -4)
s = Solution()
print(s.rangeBitwiseAnd(m, n))
