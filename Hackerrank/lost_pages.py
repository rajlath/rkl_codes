def getdiff(n):
    odds, evens = 0, 0
    while n > 0:
        n, digit = divmod(n, 10)
        if n != 0:
            odds += digit
        else:
            evens += digit
    return abs(odds - evens)



for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            room_number = i+j

            ans += getdiff(int(room_number))
    print(ans)