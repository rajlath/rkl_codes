noe = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr)
x = [noe//2-1, noe//2][noe%2==1]
print(arr[x])
