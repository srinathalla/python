class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k:
            return "0"

        res = []
        for c in num:
            while k > 0 and len(res) > 0 and res[len(res) - 1] > c:
                res.pop()
                k -= 1

            res.append(c)

        while k > 0:
            res.pop()
            k -= 1
        i = 0
        while res[i] == '0':
            i += 1
        res = res[i:]

        return ''.join(res)


s = Solution()
print(s.removeKdigits("1432219", 3))
