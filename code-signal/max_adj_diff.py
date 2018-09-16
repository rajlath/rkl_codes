def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[i] - inputArray[i-1]) for i in range(1, len(inputArray))])



print(arrayMaximalAdjacentDifference([2,4,1, 0]))