class Solution:
    def countDigitOne(self, n: int) -> int:

        def getOnesCount(n):
            count = 0
            while n > 0:
                reminder = n % 10
                if reminder == 1:
                    count += 1
                n = n//10
            return count

        sum = 0
        for i in range(1, n+1):
            sum += getOnesCount(i)

        return sum


s = Solution()
print(s.countDigitOne(13))
