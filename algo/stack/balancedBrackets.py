from collections import deque

#
# T.C : O(n) where n is the length of the string.
# #


def balancedBrackets(string):
    stack = deque()

    for ch in string:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False

        elif ch == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False

        elif ch == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False

    return len(stack) == 0


print(balancedBrackets("()[]{}{"))

print(balancedBrackets("((){{{{[]}}}})"))
