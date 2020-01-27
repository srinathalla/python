from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        self.generate(0, 0, n, result, "")
        return result

    def generate(self, open, closed, n, result, curr) -> List[str]:

        if open == closed == n:
            result.append(curr)
            return

        if open < n:
            self.generate(open + 1, closed, n, result, curr + '(')
        if closed < open:
            self.generate(open, closed + 1, n, result, curr + ')')


s = Solution()

print(s.generateParenthesis(3))
