a, b, c , x, y = [int(x) for x in input().split()]
if (a + b + c) != (x+ y):
    print("NO")
elif x > a + b or y > c + b:print("NO")
else:
    print("YES")



