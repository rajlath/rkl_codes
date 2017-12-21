'''
3 4
1 2 3
0 1 L
1 3 L
2 1 R
1 5 L
'''
from collections import defaultdict
noe, noq = [int(x) for x in input().split()]
types    = [int(x) for x in input().split()]
type_dict= defaultdict(tuple)
for i, v in enumerate(types):
    if i not in type_dict:
        type_dict[i] = []
        type_dict[i] = (i, types[(i -1 + noe) % noe], types[(i + 1) % noe])
for _ in range(noq):
    s, e, d = [x for x in input().split()]
    s = int(s)
    e = int(s)
    if s not in type_dict:
        ans = -1
    else:
        moves = 0
        start = type_dict[s][0]
        while True:
            if d == "R":
                curr = start
                if type_dict[curr][2] == e:
                    ans = type_dict[curr][0] - type_dict[start][0]
                    break
                elif type_dict[curr][0] == type_dict[start][0]:
                    ans = -1
                    break
                else:
                    curr = (curr + 1)%noe
            else:
                curr = start
                if type_dict[curr][1] == e:
                   ans = type_dict[curr][0] - type_dict[start][0]
                   break
                elif type_dict[curr][0] == type_dict[start][0]:
                        ans = -1
                        break
                else:
                    curr = (curr - 1 + noe) % noe
    print(ans)
















