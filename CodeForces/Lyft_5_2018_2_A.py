n= int(input())
x, y = [int(x) for x in input().split()]
a = max(x-1, y-1)
b = max(n-x, n-y)
print(["White", "Black"][a > b])
