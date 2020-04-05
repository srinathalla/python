class Solution:
    def parseTernary(self, e: str) -> str:

        n = len(e)
        stack = []
        for i in range(n)[::-1]:
            c = e[i]
            if len(stack) > 0 and stack[-1] == '?':
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()

                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return stack[-1]


s = Solution()
print(s.parseTernary("F?1:T?4:5"))
