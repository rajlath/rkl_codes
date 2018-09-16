primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for _ in range(int(input())):
    noe = int(input())
    ele = sorted([int(x) for x in input().split()])
    ans = -1
    if ele[0] == 1:
        for i in ele[1:]:
            if i in primes:
                ans = i
                break
    print(ans)


