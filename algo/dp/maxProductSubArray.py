from typing import List


class Solution:

    #
    # Naive approach T.C : O(n)
    # S.C : O(1)
    #
    # #
    def maxProductWithSwap(self, nums: List[int]) -> int:
        gmax = nums[0]
        cmax = nums[0]
        cmin = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                t = cmax
                cmax = cmin
                cmin = t

            cmax = max(cmax * nums[i], nums[i])
            cmin = min(cmin * nums[i], nums[i])

            gmax = max(gmax, cmax)

        return gmax

   #
    # Naive approach T.C : O(n)
    # S.C : O(1)
    #
    # #
    def maxProduct(self, nums: List[int]) -> int:

        cmax = nums[0]
        cmin = nums[0]
        pmax = nums[0]
        pmin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cmax = max(pmax * nums[i], pmin * nums[i], nums[i])
            cmin = min(pmax * nums[i], pmin * nums[i], nums[i])

            pmax = cmax
            pmin = cmin

            ans = max(ans, cmax)

        return ans


s = Solution()
print(s.maxProduct([-2, 3, -4]))
