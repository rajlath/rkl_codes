nots = int(input())

for _ in range(nots):
    ans = "Yes"
    lens = int(input())
    s = input()
    for i in range(lens//2):
        pair = s[lens - i - 1]
        if pair is "?":continue
        if s[i] != pair:
            ans = "No"
            break
    print(ans)
