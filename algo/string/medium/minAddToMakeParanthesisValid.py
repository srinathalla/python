class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = 0
        bal = 0

        for c in S:
            bal += 1 if c == '(' else -1

            if bal < 0:
                ans += 1
                bal += 1
        return ans + bal


s = Solution()

print(s.minAddToMakeValid(")))"))
