class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        x = n
        while x != 1:
            visited.add(x)
            sum = 0
            while x > 0:
                rem = x % 10
                sum += rem*rem
                x = x//10

            if sum in visited:
                return False
            x = sum

        return True


s = Solution()
print(s.isHappy(19))
