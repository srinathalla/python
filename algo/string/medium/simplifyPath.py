class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        skip = {"..", ".", ""}

        items = path.split('/')

        for item in items:
            if item == ".." and stack:
                stack.pop()
            elif item not in skip:
                stack.append(item)

        res = ""
        while stack:
            res = '/' + stack.pop() + res

        return '/' if res == "" else res


s = Solution()

print(s.simplifyPath("/../"))
