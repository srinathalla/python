
import collections


def countPatterns(n):

    return 24**n - 9*(8**n) + 18*(3**n) + 9*(2**n) - 24


print(countPatterns(2))
