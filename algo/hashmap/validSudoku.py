from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    b = '(' + board[i][j] + ')'
                    if b + str(i) in seen or str(j) + b in seen or str(i//3) + b + str(j//3) in seen:
                        return False

                    seen.add(b + str(i))
                    seen.add(str(j) + b)
                    seen.add(str(i//3) + b + str(j//3))
        return True


s = Solution()
g = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", "3", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(s.isValidSudoku(g))
