lens = int(input())
seats = [int(x) for x in input().split()]
alice = seats[0]
needs = sum(seats) // 2 + 1
answer = [1]
got = alice
for i in range(1, lens):
    if seats[i] <= alice // 2:
        answer.append(i  + 1)
        got += seats[i]
        if got >= needs:
            break
if got < needs:
    print(0)
else:
    print(len(answer))
    print(*answer)
        