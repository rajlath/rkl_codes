lens = int(input())
given = input()
rooms = [0] * 10
for i in given:
    if i == "L":
        rooms[rooms.index(0)] = 1
    elif i == "R":
        rooms[9 - rooms[::-1].index(0)] = 1
    else:
        rooms[int(i)] = 0

print("".join(map(str,rooms)))
