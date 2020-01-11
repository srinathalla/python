from typing import List

#
# This problem is similar to longest sub array with two distinct characters..
#
# T.C : O(2n) => O(n) Two pass solution
# S.C : O(3) => O(1) as map holds only 3 entries at max
# #


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) < 3:
            return len(tree)

        left = 0
        right = 0
        maxVal = [-1, -1]
        count = 0
        fruitsMap = {}
        while right < len(tree):
            if tree[right] not in fruitsMap:
                fruitsMap[tree[right]] = 0

            if fruitsMap[tree[right]] == 0:
                count += 1

            fruitsMap[tree[right]] += 1

            while count > 2:
                fruitsMap[tree[left]] -= 1
                if fruitsMap[tree[left]] == 0:
                    count -= 1
                left += 1

            if maxVal[1] - maxVal[0] < right + 1 - left:
                maxVal[1] = right + 1
                maxVal[0] = left

            right += 1
        return maxVal[1] - maxVal[0]


s = Solution()
print(s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
