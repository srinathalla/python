class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        res = ['a'] * n
        k -= n

        while k > 0:
            if ord(res[n-1]) < ord('z'):
                res[n-1] = chr(ord(res[n-1]) + 1)
                k -= 1
            else:
                n -= 1

        return ''.join(res)


s = Solution()


print(s.getSmallestString(3, 27))
