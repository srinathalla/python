class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)

        def valid(i, j):
            if i > 1 and num[0] == '0':
                return False

            if j > 1 and num[i] == '0':
                return False

            x1 = int(num[0:i])
            x2 = int(num[i:i+j])
            s = ""
            k = i + j

            while k < len(num):
                x2 = x1 + x2
                x1 = x2 - x1
                s = str(x2)
                if num[k:].startswith(s) is False:
                    return False

                k += len(s)

            return True

        for i in range(1, n//2 + 1):
            for j in range(1, n//2 + 1):

                if num[0] == '0' and i > 1:
                    return False

                if max(i, j) > n - i - j:
                    break

                if valid(i, j):
                    return True
        return False


s = Solution()
print(s.isAdditiveNumber("123"))
