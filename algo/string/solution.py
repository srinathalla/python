class Solution:
    def lengthOfLongestSubsing(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        maxLen = 1
        start = 0
        seen = {}
        seen[s[0]] = 0

        for i in range(1, len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)
            if maxLen < i + 1 - start:
                maxLen = i + 1 - start
            seen[s[i]] = i

        return maxLen


s = Solution()

print(s.lengthOfLongestSubsing("au"))
print(s.lengthOfLongestSubsing("abcabc"))
