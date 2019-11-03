for _ in range(int(input())):
    a, b, c = [pow(int(x),2) for x in input().split()]
    ans = "Not a right-angled triangle"
    if a + b == c or a + c == b or b + c ==  a:
        ans = "Right-angled triangle"
    print(ans)