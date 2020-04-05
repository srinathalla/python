from collections import Counter


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        def delete(board):
            i = 0
            for j in range(len(board)):
                if board[i] == board[j]:
                    continue
                if j - i >= 3:
                    return delete(board[:i] + board[j:])
                i = j

            return board

        def dfs(board, c):

            board = delete(board)
            if board == "#":
                return 0
            mc = 6
            i = 0
            for j in range(len(board)):
                if board[i] == board[j]:
                    continue
                need = 3 - (j - i)
                if c[board[i]] >= need:
                    c[board[i]] -= need
                    mc = min(mc, need + dfs(board[:i] + board[j:], c))
                    c[board[i]] += need
                i = j

            return mc

        c = Counter(hand)
        res = dfs(board + '#', c)
        return -1 if res == 6 else res


board = "WWRRBBWW"
hand = "WRBRW"
s = Solution()
print(s.findMinStep(board, hand))
