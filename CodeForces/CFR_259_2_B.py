lens = int(input())
given = [int(x) for x in input().split()]
answer = 0
for i in range(1, lens):
    if given[i] < given[i - 1]:
        if given[i:] + given[:i] == sorted(given):
            answer = lens - i
        else:
            answer = -1
            break
print(answer)
