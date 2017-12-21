import bisect
def count_inv(arr):
    inv_count = 0;
    i = 0
    j = len(arr)//2
    k = len(arr)
    while (i <= j - 1):
        if (arr[i] <= arr[j]):
            i+=1
            continue
        else:
            inv_count = inv_count + (j - i)
        i+=1
    return inv_count


def bruteforce_loops_PM2R(a):
    total = 0
    for i in range(1, len(a)):
        u = a[i]
        for j in range(i):
            if a[j] > u:
                total += 1
    return total

def bruteforce_sum_PM2R(a):
    return sum(1 for i in range(1, len(a)) for j in range(i) if a[j] > a[i])

def solution_TimBabych(A):
    sorted_left = []
    res = 0
    for i in range(1, len(A)):
        bisect.insort_left(sorted_left, A[i-1])
        # i is also the length of sorted_left
        res += (i - bisect.bisect(sorted_left, A[i]))
    return res

for i in range(int(input())):
    nos = int(input())
    arr = [int(x) for x in input().split()]

    for i in range(nos):
        arr = arr[1:]+arr[:1]
        print(arr)
        #d.rotate(1)
       #print(arr)
       # print(count_inv(arr),end = " ")
        print(solution_TimBabych(arr),end=" ")
    print()