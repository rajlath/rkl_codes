def extractEachKth(inputArray, k):
    ans = []
    i   = 0
    while len(inputArray)>0:
        while i < k-1 and len(inputArray)>0:
            ans.append(inputArray.pop(0))
            i += 1
        if len(inputArray)> 0:inputArray.pop(0)
        i = 0
    return ans

print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

return [n for i, n in enumerate(inputArray) if (i+1) % k != 0]