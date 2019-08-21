def longestUncorruptedSegment(sourceArray, destinationArray):
    current = [0, 0] # first = length second = index
    longest = [0, 0]

    for i, v in enumerate(sourceArray):
        if sourceArray[i] == destinationArray[i]:
            current[0] += 1
            continue
        if current[0] > longest[0]:
            longest[0] = current[0]
            longest[1] = current[1]
            current = [0, i + 1]
    if current[0] > longest[0]:
        longest[0] = current[0]
        longest[1] = current[1]
    return longest


sourceArray = [33531593, 96933415, 28506400, 39457872, 29684716, 86010806]
destinationArray = [33531593, 96913415, 28506400, 39457872, 29684716, 86010806]

print(longestUncorruptedSegment(sourceArray, destinationArray))
