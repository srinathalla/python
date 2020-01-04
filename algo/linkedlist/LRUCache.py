import unittest


class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.dll = DLL()
        self.map = {}

    def insertKeyValuePair(self, key, value):

        if key not in self.map:
            if self.dll.size() == self.maxSize:
                node = self.dll.removeFirst()
                del self.map[node.key]

            node = Node(key, value)
            self.dll.addLast(node)
            self.map[key] = node
        else:
            node = self.map[key]
            node.value = value
            self.dll.remove(node)
            self.dll.addLast(node)

    def getValueFromKey(self, key):
        if key not in self.map:
            return None

        node = self.map[key]
        self.dll.remove(node)
        self.dll.addLast(node)

        return node.value

    def getMostRecentKey(self):
        return self.dll.tail.key


class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = self.head
        self.length = 0

    def addLast(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        self.length += 1

    def removeFirst(self):
        node = self.head.next
        self.remove(node)
        return node

    def remove(self, node):
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = self.tail.prev

        self.length -= 1

    def size(self):
        return self.length


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


letterMaps = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def testLruOfSize(size, testContext):
    # Instantiate cache and insert first key.
    lru = LRUCache(size)
    testContext.assertEqual(lru.getValueFromKey("a"), None)
    lru.insertKeyValuePair("a", 99)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 99)
    # Add existing key when cache isn't full.
    lru.insertKeyValuePair("a", 0)
    testContext.assertEqual(lru.getMostRecentKey(), "a")
    testContext.assertEqual(lru.getValueFromKey("a"), 0)
    # Add keys until cache reaches maximum capacity.
    for i in range(1, size):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache isn't full.
        for j in range(0, i):
            letter = letters[j]
            testContext.assertEqual(
                lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), letterMaps[currentLetter]
        )
    # Add keys now that cache is at maximum capacity.
    for i in range(size, len(letters)):
        mostRecentLetter = letters[i - 1]
        testContext.assertEqual(lru.getMostRecentKey(), mostRecentLetter)
        # Test key retrieval when cache is full.
        for j in range(i - size, i):
            letter = letters[j]
            testContext.assertEqual(
                lru.getValueFromKey(letter), letterMaps[letter])
            testContext.assertEqual(lru.getMostRecentKey(), letter)
        leastRecentLetter = letters[i - size]
        currentLetter = letters[i]
        testContext.assertEqual(lru.getValueFromKey(currentLetter), None)
        lru.insertKeyValuePair(currentLetter, letterMaps[currentLetter])
        testContext.assertEqual(lru.getMostRecentKey(), currentLetter)
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), letterMaps[currentLetter]
        )
        testContext.assertEqual(lru.getValueFromKey(leastRecentLetter), None)
    # Add existing keys when cache is full.
    for i in range(len(letters) - size, len(letters)):
        currentLetter = letters[i]
        testContext.assertEqual(
            lru.getValueFromKey(currentLetter), letterMaps[currentLetter]
        )
        lru.insertKeyValuePair(
            currentLetter, (letterMaps[currentLetter] + 1) * 100)
        testContext.assertEqual(
            lru.getValueFromKey(
                currentLetter), (letterMaps[currentLetter] + 1) * 100
        )


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testLruOfSize(1, self)

    def test_case_2(self):
        testLruOfSize(2, self)

    def test_case_3(self):
        testLruOfSize(3, self)

    def test_case_4(self):
        testLruOfSize(4, self)

    # def test_case_5(self):
        #testLruOfSize(5, self)

    # def test_case_6(self):
        #testLruOfSize(6, self)

    # def test_case_7(self):
        #testLruOfSize(7, self)

    # def test_case_8(self):
        #testLruOfSize(8, self)

    # def test_case_9(self):
        #testLruOfSize(9, self)

        # def test_case_10(self):
        #   testLruOfSize(10, self)


if __name__ == "__main__":
    unittest.main()
