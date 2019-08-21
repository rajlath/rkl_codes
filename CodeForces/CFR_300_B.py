given = int(input())
answer= []
while given != 0:
    current = ''
    for i in str(given):
        current += str(min(int(i), 1))
    given -= int(current)
    answer.append(current)
print(len(answer))
print(*answer)
