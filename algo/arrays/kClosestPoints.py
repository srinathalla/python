from typing import List

#
# T.C : O(nlogn) where n is no of points
#  #


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        points.sort(key=lambda entry: entry[0] ** 2 + entry[1] ** 2)

        return points[:K]


s = Solution()

print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
print(s.kClosest([[1, 3], [-2, 2]], 1))
