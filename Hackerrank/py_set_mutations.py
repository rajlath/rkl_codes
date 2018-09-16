'''
16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
'''
alen  = int(input())
a     = set([int(x) for x in input().split()])
q     = int(input())
for _ in range(q):
    comm = input().split()
    comms= comm[0]
    lens = int(comm[1])
    s    = set([int(x) for x in input().split()])
    if comms == "intersection_update":
        a.intersection_update(s)
    elif comms == "update":
        a.update(s)
    elif comms == "symmetric_difference_update"    :
        a.symmetric_difference_update(s)
    else:
        a.difference_update(s)

print(sum(a))