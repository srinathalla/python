def minRewards(scores):
    rewards = []
    for x in scores:
        rewards.append(1)
    i = 1
    while i < len(scores):
        if (scores[i] > scores[i-1]):
            rewards[i] = rewards[i-1] + 1
        i += 1

    i = len(scores) - 2
    while i >= 0:
        if (scores[i] > scores[i+1] and rewards[i] <= rewards[i+1]):
            rewards[i] = rewards[i + 1] + 1
        i -= 1

    sum = 0
    for r in rewards:
        sum += r

    return sum
