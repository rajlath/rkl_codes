nb_Test = int(input())
for _ in range(nb_Test):
    N = int(input())
    arr = [int(x) for x in input().split()]
    A, B, C = [int(x) for x in input().split()]
    word = input()
    for i, v in enumerate(word):
        if v == "R":
            arr = arr[:i] + arr[i:][::-1]
        elif v == "A":
            for x in range(i, N):
                arr[x] += A
        elif v == "M":
            for x in range(i, N):
                arr[x] *= B
        arr = [x%C for x in arr]
        print(arr[i], end=" ")
