from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])
        found = True
        while found:
            found = False
            for i in range(n):
                for j in range(m):
                    val = abs(board[i][j])
                    if val > 0 and j < m - 2 and abs(board[i][j+1]) == val and abs(board[i][j+2]) == val:
                        board[i][j] = -val
                        board[i][j+1] = -val
                        board[i][j+2] = -val
                        found = True
                    if val > 0 and i < n - 2 and abs(board[i+1][j]) == val and abs(board[i+2][j]) == val:
                        board[i][j] = - val
                        board[i+1][j] = -val
                        board[i+2][j] = -val
                        found = True

            for j in range(m):
                r = n-1
                for i in reversed(range(n)):
                    if board[i][j] >= 0:
                        board[r][j] = board[i][j]
                        r -= 1
                for i in reversed(range(0, r+1)):
                    board[i][j] = 0

        return board


board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [
    5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]
s = Solution()
print(s.candyCrush(board))
