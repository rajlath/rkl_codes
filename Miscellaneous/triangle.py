noe = int(input())
arr = [int(x)-1 for x in input().split()]
if any(arr[arr[arr[i]]] == i for i in range(noe)):
    print("YES")
else:
    print("NO")