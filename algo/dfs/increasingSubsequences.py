from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def recurse(res, path, i, nums):

            if len(path) > 1:
                res.append(path[:])

            if i == len(nums):
                return

            used = set()
            for i in range(i, len(nums)):
                if nums[i] in used:
                    continue

                if len(path) == 0 or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    recurse(res, path, i + 1, nums)
                    path.pop()

        res = []
        path = []
        recurse(res, path, 0, nums)
        return res


s = Solution()
print(s.findSubsequences([4, 5, 7, 7]))
