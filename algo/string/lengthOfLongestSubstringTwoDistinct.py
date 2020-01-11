#
# T.C : O(2n) => O(n) using two pointers
# S.C : O(1) => As map always holds not more than three keys
# #


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        if len(s) <= 2:
            return len(s)

        maxLen = float('-inf')
        l = 0
        r = 0

        map = {}
        count = 0
        while r < len(s):
            if s[r] not in map:
                map[s[r]] = 0

            if map[s[r]] == 0:
                count += 1

            map[s[r]] += 1

            while count > 2:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    count -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen


s = Solution()

print(s.lengthOfLongestSubstringTwoDistinct("abcabcabc"))
