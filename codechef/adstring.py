'''
Input:
3
Simran Simran Lipsa Lipsa
Shruti Prats Sai Sai Shibasis
Ankit Asutosh Saurabh

Output:
YES
NO
YES
'''
from collections import Counter
ins = int(input())
for _ in range(ins):
    ins = len(set(Counter([x for x in input().split()]).values()))
    print(["NO", "YES"][ins==1])