from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> bool:

        ps = [0] * len(nums)

        ps[0] = nums[0]
        for i in range(1, len(nums)):
            ps[i] = ps[i-1] + nums[i]

        for i in range(1, len(nums)-5):
            s1 = ps[i-1]
            for j in range(i+2, len(nums)-3):
                s2 = ps[j-1] - ps[i]
                if s1 == s2:
                    for k in range(j+2, len(nums)-1):
                        s3 = ps[k-1] - ps[j]
                        s4 = ps[-1] - ps[k]
                        if s2 == s3 and s3 == s4:
                            return True

        return False


arr = [1, 2, 1, 2, 1, 2, 1]
s = Solution()
print(s.splitArray(arr))
