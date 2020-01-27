class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        result = [0 for i in range(len(num1) + len(num2))]

        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                mul = int(num1[i]) * int(num2[j])
                sum = result[i+j+1] + mul
                result[i+j] += sum//10
                result[i+j+1] = sum % 10
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1

        if i == len(result):
            return "0"

        result = result[i:]

        resultStr = ''
        for ch in result:
            resultStr = resultStr + str(ch)

        return resultStr


s = Solution()
print(s.multiply("2", "3"))
print(s.multiply("123", "456"))
print(s.multiply("0", "0"))
