class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if s is None or t is None or len(s) != len(t):
            return False

        m1 = [0 for i in range(256)]
        m2 = [0 for i in range(256)]

        for i in range(len(s)):
            ch1 = ord(s[i])
            ch2 = ord(s[i])

            if m1[ch1] != m2[ch2]:
                return False

            m1[ch1] = i + 1
            m2[ch2] = i + 1

        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
