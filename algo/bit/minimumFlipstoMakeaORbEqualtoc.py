class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        count = 0
        while a > 0 or b > 0 or c > 0:
            if c & 1 == 0:
                count += (a & 1) + (b & 1)
            else:
                count += 0 if a & 1 or b & 1 else 1
            c >>= 1
            a >>= 1
            b >>= 1
        return count


s = Solution()
print(s.minFlips(2, 6, 5))
