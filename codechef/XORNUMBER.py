for _ in range(int(input())):
    curr = int(input())
    if bin(curr)[2:].count("0")>0:
        print(-1)
    else:
        print([curr//2, 2][curr == 1])
    