class Solution:
    def longestValidParentheses(self, s: str) -> int:

        open = 0
        closed = 0

        maxLen = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                closed += 1

            if closed > open:
                closed = 0
                open = 0
            if open == closed:
                maxLen = max(maxLen, 2 * open)

        open, closed = 0, 0
        for i in reversed(range(len(s))):
            ch = s[i]
            if ch == '(':
                open += 1
            elif ch == ')':
                closed += 1

            if open > closed:
                closed = 0
                open = 0
            if open == closed:
                maxLen = max(maxLen, 2 * open)

        return maxLen

    def longestValidParenthesesUsingStack(self, s: str) -> int:

        stack = []
        stack.append(-1)

        maxLen = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[len(stack)-1])

        return maxLen


s = Solution()
print(s.longestValidParentheses("((()))"))
print(s.longestValidParentheses("(()"))
print(s.longestValidParenthesesUsingStack("((()))"))
print(s.longestValidParenthesesUsingStack("(()"))
print(s.longestValidParenthesesUsingStack(")()())"))
