class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        if len(s1) == len(s2):
            return s1 == s2
        s1 = ''.join(sorted(s1))
        print(s1)
        print(len(s2) - len(s1) + 1)
        for i in range(0, (len(s2) - len(s1) + 1)):
            ss2 = ''.join(sorted(s2[i: i + len(s1)]))
            print(ss2)
            if s1 == ss2:
                return True

        return False


s1 = "ab"
s2 = "eidbaooo"
s = Solution()
print(s.checkInclusion(s1, s2))
