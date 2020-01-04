#
#
# S.C : visisted array space + trie space => O(n*m) +  O(ws) where w : no of words, s : length of longest string.
# T.C : O(w*s) + O(n*m*8^s) n*m is the no of chars and at each char we have 8 neighbours each has 8 and so on...
#  s : length of longest string.
#
# @param {} board
# @param {*} words
#
# #


def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)

    finalWords = set()

    visited = [[False for char in board[0]] for i in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(i, j, board, visited, trie.root, finalWords)

    return list(finalWords)


def explore(i, j, board, visited, trieNode, finalWords):
    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and visited[i][j] is False and board[i][j] in trieNode:

        visited[i][j] = True
        trieNode = trieNode[board[i][j]]
        if '*' in trieNode:
            finalWords.add(trieNode['*'])

        explore(i + 1, j, board, visited, trieNode, finalWords)
        explore(i + 1, j + 1, board, visited, trieNode, finalWords)
        explore(i + 1, j - 1, board, visited, trieNode, finalWords)
        explore(i, j + 1, board, visited, trieNode, finalWords)
        explore(i, j - 1, board, visited, trieNode, finalWords)
        explore(i - 1, j, board, visited, trieNode, finalWords)
        explore(i - 1, j + 1, board, visited, trieNode, finalWords)
        explore(i - 1, j - 1, board, visited, trieNode, finalWords)

        visited[i][j] = False


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current['*'] = word


board = [
    ["f", "t", "r", "o", "p", "i", "k", "b", "o"],
    ["r", "w", "l", "p", "e", "u", "e", "a", "b"],
    ["j", "o", "t", "s", "e", "l", "f", "l", "p"],
    ["s", "z", "u", "t", "h", "u", "o", "p", "i"],
    ["k", "a", "e", "g", "n", "d", "r", "g", "a"],
    ["h", "n", "l", "s", "a", "t", "e", "t", "x"],
]
words = [
    "frozen",
    "rotten",
    "teleport",
    "city",
    "zutgatz",
    "kappa",
    "before",
    "rope",
    "obligate",
    "annoying",
]
expected = [
    "frozen",
    "rotten",
    "teleport",
    "kappa",
    "before",
    "rope",
    "obligate",
]
print(boggleBoard(board, words))
