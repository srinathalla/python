# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


class MountainArray:

    arr = [1, 2, 3, 4, 5, 3, 1]

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def bSearch(l, r, incr):
            while l < r:
                m = l + r >> 1

                if mountain_arr.get(m) == target:
                    return m
                elif mountain_arr.get(m) > target:
                    if incr is True:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if incr is True:
                        l = m + 1
                    else:
                        r = m - 1
            return l if mountain_arr.get(l) == target else -1

        left = 0
        right = mountain_arr.length() - 1
        while left < right:
            mid = left + right >> 1
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            elif mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid

        peak = left

        res = bSearch(0, peak, True)
        if res != -1:
            return res
        else:
            return bSearch(peak, mountain_arr.length() - 1, False)


s = Solution()
print(s.findInMountainArray(3, MountainArray()))
