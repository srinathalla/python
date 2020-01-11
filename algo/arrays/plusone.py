from typing import List

#
# T.C : O(n) worst case two pas.
# #


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in reversed(range(len(digits))):
            no = digits[i] + carry
            if no == 10:
                no = 0
                carry = 1
            else:
                carry = 0

            digits[i] = no

            if carry == 0:
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits


s = Solution()

print(s.plusOne([9, 9, 9]))
