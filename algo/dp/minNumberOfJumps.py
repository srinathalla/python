#
# T.C O(n)
# S.C O(3)
#


from typing import List


def minNumberOfJumps(array):

    if len(array) < 2:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]

    for i in range(1, len(array)-1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return True

        if nums[0] == 0:
            return False

        currPos = 0
        steps = nums[0]
        maxReach = nums[0]

        for i in range(len(nums)):
            maxReach = max(maxReach, i + nums[i])

            if maxReach >= len(nums) - 1:
                return True

            steps -= 1

            if steps == 0:
                steps = maxReach - i

                if steps == 0 and i < len(nums) - 1:
                    return False

        return maxReach >= len(nums) - 1


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
