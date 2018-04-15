n, m = map(int, input().split())
squares = list(map(int, input().split()))


def calc(squares):
    x = {i+1: 0 for i in range(n)}
    for i in squares:
        x[i] += 1
    return x

x = calc(squares)

print(min(x.values()))