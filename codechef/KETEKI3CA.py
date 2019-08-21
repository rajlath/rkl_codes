for _ in range(int(input())):
    n = int(input())
    s = list(input())
    m = int(input())
    for i in range(m):
        index, val = map(int, input().split())
        s[n-index-1] = str(val)

        if s == s[::-1]:
            print("Palindrome")
        else:
            print(-1)
