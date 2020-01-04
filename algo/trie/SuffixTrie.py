# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    #
    # # T.C : O(n^2) S.C : O(n^2)
    def populateSuffixTrieFrom(self, string):

        for i in range(len(string)):
            current = self.root
            for j in range(i, len(string)):
                if string[j] not in current:
                    current[string[j]] = {}
                current = current[string[j]]
            current['*'] = True

    # T.C : O(m) m is length of string
    def contains(self, string):
        current = self.root

        for letter in string:
            if letter not in current:
                return False
            current = current[letter]
        return True if '*' in current else False


trie = SuffixTrie("babc")
print(trie.contains("abc"))

trie1 = SuffixTrie("test")
print(trie1.root)
