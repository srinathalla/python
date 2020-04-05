
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.i = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.i < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        val = self.nums[self.i]
        self.i += 1
        return val


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.nextval = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nextval if self.nextval is not None else False

    def next(self):
        ret = self.nextval
        self.nextval = self.iterator.next() if self.iterator.hasNext() else None
        return ret

    def hasNext(self):
        return True if self.nextval is not None else False


iter = PeekingIterator(Iterator([1, 2, 3]))
while iter.hasNext():
    print(iter.peek())   # Get the next element but not advance the iterator.
    print(iter.next())         # Should return the same value as [val].
