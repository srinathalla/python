class Solution:
    def reverse(self, x: int) -> int:

        rev = 0
        i = 0
        symbol = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            reminder = x % 10
            x = x // 10

            rev = rev*10 + reminder

        return rev*symbol if rev < 2**31 else 0


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
