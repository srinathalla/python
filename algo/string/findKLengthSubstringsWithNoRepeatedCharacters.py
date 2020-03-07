class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        return sum([1 for i in range(len(S) - K + 1) if len(S[i:i+K]) == len(set(S[i:i+K]))])


s = Solution()
print(s.numKLenSubstrNoRepeats("havefunonleetcode", 5))
