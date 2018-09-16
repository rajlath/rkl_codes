def arrayChange(inputArray):
    curr = inputArray[0]
    curr -= 1
    ans = 0
    for nexts in inputArray:
        curr = max(curr+1, nexts)
        ans  += curr - nexts
    return ans

print(arrayChange([1,1,1]))