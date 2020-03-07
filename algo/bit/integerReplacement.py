
#
# Idea is two consecutive nos when tried reach 1 even no will reach in less no of steps than odd.
#  #


class Solution:
    def integerReplacement(self, n: int) -> int:

        count = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                if (n + 1) % 4 == 0 and n - 1 != 2:
                    n += 1
                else:
                    n -= 1
            count += 1
        return count
