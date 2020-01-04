def underscorifySubstring(string, substring):
    i = 0
    start = 0
    result = []
    while i < len(string):
        j = 0
        while i < len(string) and string[i] != substring[j]:
            result.append(string[i])
            i += 1

        start = i
        appendUnderScore = False
        while i < len(string) and string[i] == substring[j]:
            i += 1
            j += 1

            if j == len(substring):
                appendUnderScore = True
                j = 0

        if appendUnderScore:
            result.append('_')

        while start < i - j:
            result.append(string[start])
            start += 1

        if appendUnderScore:
            result.append('_')

        while start < i:
            result.append(string[start])
            start += 1
    return "".join(result)


print(underscorifySubstring(
    "testthis is a testest to see if testestes it works", "test"))
