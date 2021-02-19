class Solution:
    def findIntegers(self, num: int) -> int:

        f = [0] * 32
        f[0] = 1
        f[1] = 2

        for i in range(2, 32):
            f[i] = f[i-1] + f[i-2]

        k = 30
        ans = 0
        pbit = 0

        print(f)
        while k >= 0:
            if (num & (1 << k)) > 0:
                ans += f[k]

                if pbit == 1:
                    return ans

                pbit = 1
            else:
                pbit = 0

            k -= 1

        return ans + 1


s = Solution()
print(s.findIntegers(5))
