'''
def find_min_rec(arr, i, sum_calc, sum_total):
    if i == 0: return abs((sum_total - sum_calc) - sum_calc)
    return min(find_min_rec(arr, i-1, sum_calc+arr[i-1], sum_total), find_min_rec(arr, i-1, sum_calc, sum_total))

def find_mi(arr, n):
    sum_total = sum(arr)
    return find_min_rec(arr, n, 0, sum_total)

n = int(input())
print(find_mi(range(1, n+1), 4))


def find_min(arr, n):
    sums = sum(arr)
    dp = []
    for i in range(n+1):
        lst = []
        for j in range(sums+1):
            lst.append(j)
        dp.append(lst)

    for i in range(1, sums+1):
        dp[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, sums+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    diff = 10e9
    j = sums//2
    while j > 0:
        if dp[n][j]:
            diff = sums - 2*j
            break
        j-=1
    return diff

print(find_min(range(1, 5), 4))
'''
import itertools as it
def min_diff_sets(data):
    if len(data) == 1:
        return data[0]
    s = sum(data)

    a = []
    for i in range(1, len(data)):
        a.extend(list(it.combinations(data, i)))
    b = it.combinations(a, 2)
    c = filter(lambda x: sum(x[0])+sum(x[1])==s, b)
    c = filter(lambda x: sorted([i for sub in x for i in sub])==sorted(data), c)
    res = sorted([(abs(sum(i[0]) - sum(i[1])), i) for i in c],
            key=lambda x: x[0])
    return (res[0][0], res[0][1])


n = int(input())
mins, minlst = min_diff_sets(range(1, n+1))
print(mins)
print(" ".join(map(str, minlst[0])))







