'''
2 2
main 192.168.0.2
replica 192.168.0.1
block 192.168.0.1;
proxy 192.168.0.2;
'''
from collections import defaultdict
server_dict = defaultdict(str)
servers, command = [int(x) for x in input().split()]
for i in range(servers):
    s, i = [x for x in input().split()]
    server_dict[i] = s

for i in range(command):
    inp = input()
    serv, ip = inp.split()
    ip = ip[:-1]
    print(inp + " #"+ server_dict[ip])

