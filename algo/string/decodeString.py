from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr, currCount = "", 0

        for c in s:
            if c == '[':
                stack.append(currStr)
                stack.append(currCount)
                currStr = ""
                currCount = 0

            elif c == ']':
                count = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + currStr * count
            elif c.isdigit():
                currCount = currCount*10 + int(c)
            else:
                currStr += c

        return currStr


s = Solution()


s1 = "3[a]2[bc]"
print(s.decodeString(s1))
s1 = "3[a2[c]]"
print(s.decodeString(s1))
s1 = "2[abc]3[cd]ef"
print(s.decodeString(s1))
