def waterArea(heights):  
    left = []

    maxValue = 0
    for i in range(len(heights)):
        maxValue = max(maxValue, heights[i])
        left.append(maxValue)
    
    maxValue = 0
    sum = 0
    for i in reversed(range(len(heights))):
        maxValue = max(maxValue, heights[i])
        sum += min(left[i],maxValue) - heights[i]
    
    return sum

print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))


    
