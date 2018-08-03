'''
Examples
inputCopy
4
24 21 14 10
outputCopy
3
inputCopy
2
500 500
outputCopy
0
inputCopy
3
14 5 1
outputCopy
-1
inputCopy
5
1 3 6 9 12
outputCopy
1

noe = int(input())
arr = [int(x) for x in input().split()]
if noe == 1 or noe ==2:
    print(0)
else:

    ap_sum = (noe * (arr[0] + arr[-1])) // 2
    print(ap_sum, sum(arr))
    if ap_sum == sum(arr):
        print(0)
    else:
        diff = ap_sum - sum(arr)
        if diff > noe//2:
            print(-1)
        else:
            print(diff//2)
'''
# Python 3 Program to find
# mean absolute deviation
# of given array.

# Function to find mean
# of the array elements.
def Mean(arr, n) :

    # Calculate sum of all
    # elements.
    sm = 0

    for i in range(0, n) :
        sm = sm + arr[i]
    return sm // n

# Function to find mean
# absolute deviation of
# given elements.
def meanAbsoluteDeviation(arr, n) :

    # Calculate the sum of
    # absolute deviation
    # about mean.
    absSum = 0
    for i in range(0, n ):
        absSum = absSum + abs(arr[i] -
                         Mean(arr, n))

    # Return mean absolute
    # deviation about mean.
    return absSum / n

print(meanAbsoluteDeviation([1, 3, 6, 9, 12], 5))



