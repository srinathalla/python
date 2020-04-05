from typing import List


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:

        if len(words1) != len(words2):
            return False

        g = {}
        for pair in pairs:
            if pair[0] not in g.keys():
                g[pair[0]] = []

            if pair[1] not in g.keys():
                g[pair[1]] = []

            g[pair[0]].append(pair[1])
            g[pair[1]].append(pair[0])

        def dfs(g, word, c, map):
            map[word] = c
            for aw in g[word]:
                if aw not in map.keys():
                    dfs(g, aw, c, map)

        cc = {}
        c = 0
        for w in g.keys():
            if w not in cc.keys():
                dfs(g, w, c, cc)
                c += 1

        for i in range(len(words1)):
            if words1[i] != words2[i] and cc.get(words1[i], -1) != cc.get(words2[i], -2):
                return False

        return True


w1 = ["I", "have", "enjoyed", "happy", "thanksgiving", "holidays"]
w2 = ["I", "have", "enjoyed", "happy", "thanksgiving", "holidays"]

pairs = [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"], ["vehicle", "car"], [
    "entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"], ["actually", "very"], ["really", "very"], ["super", "very"]]
s = Solution()
print(s.areSentencesSimilarTwo(w1, w2, pairs))
