def avoidObstacles(inputArray):
    i = 2
    while any(x%i==0 for x in inputArray):
        i += 1
    return i


print(avoidObstacles([5, 3, 6, 7, 9]))