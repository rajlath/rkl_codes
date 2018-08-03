import bisect
nor, nol = [int(x) for x in input().split()]
room_size= [int(x) for x in input().split()]
letters  = [int(x) for x in input().split()]
rooms = [0]
for i in range(nor):
    rooms.append(room_size[i] + rooms[-1])
for l in letters:
    i = bisect.bisect(rooms, l-1)
    print(i, l - rooms[i-1])




