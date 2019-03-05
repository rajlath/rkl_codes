input()
a=[*map(int,input().split())]
m=max(a)
l=len(max(''. join(["." if x == m else " " for x in a]).split(), key=len))
print(l)