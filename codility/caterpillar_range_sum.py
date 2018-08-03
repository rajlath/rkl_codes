arr = [6,2,7,4,1,3,6,11, 23, 56, 7, 8, 91]
sums= 80

def caterpillar_sum(arr, sums):
    lens  = len(arr)
    front = 0
    asum  = 0
    for curr in range(lens):
        while (front < lens and (asum + arr[front]) <= sums):
            asum  += arr[front]
            front += 1
        if asum == sums:
            print(front, curr)
            return True
        asum -= arr[curr]
    return False
'''
def caterpillarMethod(A, s):
    n = len(A)
    front, total = 0, 0
    for back in range(n):
        while (front < n and total + A[front] <= s):
            total += A[front]
            front += 1
        if total == s:
            print(front, back)
            return True
        total -= A[back]
    return False
'''
print(caterpillar_sum(arr, sums))