class Solution:
    def crackSafe(self, n: int, k: int) -> str:

        s = ['0'] * n
        v = set()
        v.add(''.join(s))
        tc = pow(k, n)

        def dfs(s, v, tc):
            if len(v) == tc:
                return True

            i = 0

            while i < k:
                ss = s[len(s) - n + 1:]
                ch = chr(ord('0') + i)
                ss.append(ch)
                substr = ''.join(ss)

                if substr not in v:
                    v.add(substr)
                    s.append(ch)
                    if dfs(s, v, tc) == True:
                        return True

                    s.pop()
                    v.remove(substr)

                i += 1

            return False

        dfs(s, v, tc)
        return ''.join(s)


s = Solution()
print(s.crackSafe(2, 2))
