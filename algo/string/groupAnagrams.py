#
# T.C : O(w*nlogn) where n : length of longest word and w : no of words
# S.C : O(w*n)
#  #


def groupAnagrams(words):
    map = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord not in map:
            map[sortedWord] = []
        map[sortedWord].append(word)

    return list(map.values())


print(groupAnagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
