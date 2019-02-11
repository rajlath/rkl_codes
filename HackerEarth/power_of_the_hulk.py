'''
from collections import Counter,  defaultdict
s = input()
counts = defaultdict(int)
subs = []
for i in range(len(s)):
    for j in range(i, len(s)):
        curr = s[i:j+1]
        counts[curr] += 1

#print(Counter(counts.values()))
count = Counter(counts.values())

nb_qry = int(input())
for _ in range(nb_qry):
    l, r = [int(x) for x in input().split()]
    sums = 0
    for i in range(l, r+1):
            sums += count[i]
    print(sums)
'''
for (int y = 0; y &lt; sf.Length; y++)
{
    c[y] += (ss[x].Length - ss[x].Replace(sf[y], String.Empty).Length) / sf[y].Length;
}

s = input()
for y in range(len(s)):
    c[y] = 

