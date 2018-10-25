'''
Input

2
4
15 25 30 35 45 50 10 20
2
15
25

10
10 15 5 12 40 55 1 10 25 35 45 50 20 28 27 35 15 40 4 5
3
5
10
27
'''
from collections import defaultdict
import os


fins = os.path.join(os.path.dirname(__file__), "large.in")
fout = os.path.join(os.path.dirname(__file__), "large.out")


in_file = open(fins, "r")
out_file= open(fout, "w")

no_test_case = int(in_file.readline().strip())


for case in range(no_test_case):
    nob = int(in_file.readline().strip())
    busl= in_file.readline().strip().split(" ")
    #print(busl)
    bus = [int(x) for x in busl]
    connection = defaultdict(list)
    bus_nos = 1
    i = 0
    while bus_nos <= nob:
        start = bus[i]
        end   = bus[i+1]
        i += 2
        for j in range(start, end+1):
            connection[j].append(bus_nos)
        bus_nos += 1
    query = int(in_file.readline().strip())
    con = []
    for i in range(query):
        conn = connection[int(in_file.readline().strip())]
        con.append(len(conn))
    ans = " ".join(map(str, con))
    #print(ans)
    out_file.write("Case #{}: {}".format(case+1, ans))
    out_file.write("\n")
    in_file.readline()




'''
for _ in range(int(input())):
    nob = int(input())
    bus = [int(x) for x in input().split()]
    connection = defaultdict(list)
    busNos = 1
    i = 0
    while busNos <= nob:
        start = bus[i]
        end   = bus[i+1]
        i += 2
        for j in range(start, end+1):
            connection[j].append(busNos)
        busNos += 1
    for _ in range(int(input())):
        conn = connection[int(input())]
        print(len(conn), end=" ")
'''





