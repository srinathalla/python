class Solution:
    def countArrangement(self, n: int) -> int:

        arr = [i for i in range(n+1)]
        self.res = 0

        def bc(arr, i):
            if i == n + 1:
                self.res += 1

            for j in range(i, n+1):
                if i % arr[j] == 0 or arr[j] % i == 0:

                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp

                    bc(arr, i+1)

                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp
        bc(arr, 1)
        return self.res


s = Solution()
print(s.countArrangement(3))
