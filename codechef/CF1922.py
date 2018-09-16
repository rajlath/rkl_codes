for _ in range(int(input())):
    nol = int(input())
    arr = [1] + [int(x) for x in input().split()] + [1]
    cnt = 0
    for i in range(1, nol):
        a, b, c = arr[i-1], arr[i], arr[i+1]
        if max(a, c) < b and a is not 0 and b is not 0:
            if b%a == 0 and  b%c == 0:
                cnt += 1
    print(cnt)





